from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from author import Author
    from magazine import Magazine

class Article:
    def __init__(self, author: Author, magazine: Magazine, title: str) -> None:
        self._author = None
        self._magazine = None
        self._title = None
        self.title = title  # Must set title first due to validation
        self.author = author
        self.magazine = magazine

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be 5-50 characters")
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Cannot modify title after creation")
        self._title = value

    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value: Author) -> None:
        from author import Author
        if not isinstance(value, Author):
            raise ValueError("Must assign an Author instance")
        self._author = value
        if self not in value._articles:
            value._articles.append(self)

    @property
    def magazine(self) -> Magazine:
        return self._magazine

    @magazine.setter
    def magazine(self, value: Magazine) -> None:
        from magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Must assign a Magazine instance")
        self._magazine = value
        if self not in value._articles:
            value._articles.append(self)

    def __repr__(self) -> str:
        return f"Article(title='{self.title}', author={self.author}, magazine={self.magazine})"