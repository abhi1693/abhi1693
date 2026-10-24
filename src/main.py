from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from fetch import fetch_articles

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    environment = Environment(
        loader=FileSystemLoader(ROOT / 'templates'),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        trim_blocks=True,
    )
    document = environment.get_template('template.md.j2').render(
        articles=fetch_articles(), updated=datetime.now(timezone.utc),
    )
    (ROOT / 'README.md').write_text(document, encoding='utf-8')


if __name__ == '__main__':
    main()
