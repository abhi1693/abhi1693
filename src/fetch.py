from datetime import datetime, date
from html import unescape
from html.parser import HTMLParser
from os import getenv
import re
from typing import Mapping
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from requests import get

from model import Post, Video

__all__ = ['fetch_posts', 'fetch_video', 'BIO']

BIO = """
If you’ve ever debugged at 3 AM, rewritten the same config for the tenth time, or felt the thrill of a green build
after hours of chaos, you’re one of us.

This page is for the tinkerers, the automators, the late-night problem solvers who’d rather script it than suffer it.

I break down real-world systems, simplify complex tech, and share hands-on solutions with zero fluff and maximum nerd
cred, all documented at https://blog.abhimanyu-saharan.com[blog.abhimanyu-saharan.com].

By supporting me at https://www.patreon.com/asaharan[patreon.com/asaharan], you’re not just fueling 
the content, you’re helping keep it raw, honest, and independent. No corporate filters. Just practical insights, 
deep dives, and the occasional war story.

Join the tribe. Let’s build, break, and fix, with purpose.
"""

_CONTENT_ENCODED_TAG = "{http://purl.org/rss/1.0/modules/content/}encoded"


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data:
            self._parts.append(data)

    def get_text(self) -> str:
        return " ".join(self._parts)


def _html_to_text(raw_html: str) -> str:
    parser = _HTMLTextExtractor()
    parser.feed(raw_html)
    parser.close()
    text = re.sub(r"\s+", " ", unescape(parser.get_text())).strip()
    return re.sub(r"\s+([.,!?;:])", r"\1", text)


def _summarize(text: str, *, max_words: int = 40) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]).rstrip() + "…"


def fetch_posts() -> list[Post]:
    url = "https://blog.abhimanyu-saharan.com/posts/rss.xml"
    headers: Mapping[str, str | bytes] | None = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    text_response: str = get(url, headers=headers).content.decode("utf-8")
    root: Element = ElementTree.fromstring(text_response)
    nodes: list[Element] = root.findall("./channel/item")[:7]

    def text_or_none(node: Element, tag: str) -> str | None:
        result: Element | None = node.find(tag)
        if result is None or result.text is None:
            return None
        text = result.text.strip()
        return text or None

    def text_or_raise(node: Element, tag: str) -> str:
        text = text_or_none(node, tag)
        if text is None:
            raise ValueError(f"Tag '{tag}' not found in node {node.tag}")
        return text

    def description_for(node: Element) -> str:
        description = text_or_none(node, "description")
        if description is not None:
            return description

        encoded = text_or_none(node, _CONTENT_ENCODED_TAG)
        if encoded is None:
            return ""
        return _summarize(_html_to_text(encoded))

    return [
        Post(
            title=text_or_raise(node, "title"),
            link=text_or_raise(node, "link"),
            description=description_for(node),
            published_date=datetime.strptime(text_or_raise(node, "pubDate"), "%a, %d %b %Y %H:%M:%S %Z"),
        )
        for node in nodes
    ]


def fetch_video() -> Video:
    playlist_id = "PLgyhMyHrtzDhX6RqKdy30NSs_hKqzAjM1"
    api_key = getenv("YOUTUBE_API_KEY")

    if api_key:
        url = (
            "https://www.googleapis.com/youtube/v3/playlistItems"
            f"?part=snippet&maxResults=1&playlistId={playlist_id}&key={api_key}"
        )
        response = get(url).json()
        try:
            snippet = response["items"][0]["snippet"]
            return Video(snippet["resourceId"]["videoId"], snippet["title"])
        except (KeyError, IndexError, TypeError):
            pass

    url = f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}"
    headers: Mapping[str, str | bytes] = {"User-Agent": "Mozilla/5.0"}
    text_response: str = get(url, headers=headers).content.decode("utf-8")
    root: Element = ElementTree.fromstring(text_response)
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
    }

    entry = root.find("atom:entry", namespaces)
    if entry is None:
        raise ValueError("No video entries found in YouTube RSS feed")

    video_id = entry.findtext("yt:videoId", namespaces=namespaces)
    title = entry.findtext("atom:title", namespaces=namespaces)
    if not video_id or not title:
        raise ValueError("Missing video id/title in YouTube RSS feed")
    return Video(video_id.strip(), title.strip())
