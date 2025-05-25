from datetime import date

class Video:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

    def __repr__(self):
        return f"Video(id={self.id}, title={self.title})"

class Post:
    def __init__(self, title: str, link: str, description: str, published_date: date):
        self.title = title
        self.link = link
        self.description = description
        self.published_date = published_date

    def __repr__(self):
        return f"Post(title={self.title}, link={self.link})"
