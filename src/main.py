from datetime import datetime

from jinja2 import Environment, FileSystemLoader, Template

from fetch import *


def main() -> None:
    environment = Environment(loader=FileSystemLoader('templates/'))
    template: Template = environment.get_template('template.adoc')
    document: str = template.render(bio=BIO, posts=fetch_posts(), video=fetch_video(), updated=datetime.today())
    with open('./README.adoc', 'w') as readme:
        readme.write(document)


if __name__ == '__main__':
    main()
