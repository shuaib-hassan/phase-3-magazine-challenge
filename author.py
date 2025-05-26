from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from magazine import Magazine
    from article import Article

class Author:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []
        Author._all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from article import Article
        if not isinstance(magazine, Magazine):
            raise ValueError("Must provide a Magazine instance")
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})

    def __repr__(self):
        return f"Author(name='{self.name}')"