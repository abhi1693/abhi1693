from datetime import datetime, date
from os import getenv
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


def fetch_posts() -> list[Post]:
    url = "https://blog.abhimanyu-saharan.com/posts/rss.xml"
    headers: Mapping[str, str | bytes] | None = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    text_response: str = get(url, headers=headers).content.decode("utf-8")
    root: Element = ElementTree.fromstring(text_response)
    nodes: list[Element] = root.findall("./channel/item")[:3]

    def text_or_raise(node: Element, tag: str) -> str:
        result: Element | None = node.find(tag)
        if result is None:
            raise ValueError(f"Tag '{tag}' not found in node {node.tag}")
        text: str | None = result.text
        if text is None:
            raise ValueError(f"Text for tag '{tag}' in node {node.tag} is None")
        return text.strip()

    return [
        Post(
            title=text_or_raise(node, "title"),
            link=text_or_raise(node, "link"),
            description=text_or_raise(node, "description"),
            published_date=datetime.strptime(text_or_raise(node, 'pubDate'), "%a, %d %b %Y %H:%M:%S %Z"),
        )
        for node in nodes
    ]


def fetch_video() -> Video:
    url = (f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=1'
           f'&playlistId=PLgyhMyHrtzDhX6RqKdy30NSs_hKqzAjM1&key={getenv("YOUTUBE_API_KEY")}')
    response = get(url).json()
    snippet = response['items'][0]['snippet']
    return Video(snippet['resourceId']['videoId'], snippet['title'])
