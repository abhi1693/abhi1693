"""Fetch five recent English articles through DevFeed's public MCP."""

import json
import re
from datetime import datetime
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit

from requests import Session

MCP_URL = 'https://mcp.devfeed.tech/mcp'
ARTICLE_LIMIT = 5


def _rpc(session: Session, request_id: int, method: str, params: dict) -> dict:
    response = session.post(
        MCP_URL,
        json={'jsonrpc': '2.0', 'id': request_id, 'method': method, 'params': params},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if 'error' in payload:
        raise RuntimeError(f"DevFeed MCP request failed: {payload['error']}")
    return payload['result']


def markdown_text(value: str) -> str:
    text = ' '.join(unescape(value).split())
    return ''.join(f'&#{ord(char)};' if char in '&[]{}<>*_`\\' else char for char in text)


class _PreviewText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def article_preview(value: str) -> str:
    parser = _PreviewText()
    parser.feed(value)
    parser.close()
    words = ' '.join(parser.parts).split()
    preview = ' '.join(words[:45])
    if len(words) > 45:
        sentences = list(re.finditer(r'[.!?](?=\s|$)', preview))
        end = sentences[-1].end() if sentences else 0
        if len(preview[:end].split()) >= 15:
            preview = preview[:end]
        else:
            preview = preview.rstrip('.,;:') + '…'
    return markdown_text(preview)


def fetch_articles() -> list[dict[str, str]]:
    with Session() as session:
        session.headers.update({'Accept': 'application/json, text/event-stream'})
        initialized = _rpc(session, 1, 'initialize', {
            'protocolVersion': '2025-11-25',
            'capabilities': {},
            'clientInfo': {'name': 'abhi1693-profile', 'version': '1.0.0'},
        })
        session.headers['Mcp-Protocol-Version'] = initialized['protocolVersion']
        response = session.post(MCP_URL, json={
            'jsonrpc': '2.0', 'method': 'notifications/initialized',
        }, timeout=30)
        response.raise_for_status()
        result = _rpc(session, 2, 'tools/call', {
            'name': 'get_feed', 'arguments': {'limit': ARTICLE_LIMIT, 'languages': ['en']},
        })
    if result.get('isError'):
        raise RuntimeError('DevFeed MCP get_feed returned an error')
    data = result.get('structuredContent')
    if data is None:
        data = json.loads(next(block['text'] for block in result['content'] if block['type'] == 'text'))
    items = data['items'][:ARTICLE_LIMIT]
    if len(items) != ARTICLE_LIMIT:
        raise ValueError('DevFeed returned fewer than five articles; keeping the existing README')
    articles = []
    for item in items:
        url = item['canonical_url']
        if not url.startswith('https://') or any(char.isspace() or char in '[]<>"' for char in url):
            raise ValueError('DevFeed returned an invalid publisher URL')
        publishers = [source['name'] for source in item.get('sources', [])
                      if source.get('source_type') == 'publisher']
        source = publishers[0] if publishers else urlsplit(url).hostname
        published = item.get('published_at')
        date = datetime.fromisoformat(published.replace('Z', '+00:00')).strftime('%b %d, %Y') if published else ''
        articles.append({
            'title': markdown_text(item['title']),
            'url': url,
            'source': markdown_text(source or ''),
            'date': date,
            'kind': markdown_text(item.get('content_type', 'article').title()),
            'preview': article_preview(item.get('ai_summary') or item.get('summary') or ''),
        })
    return articles
