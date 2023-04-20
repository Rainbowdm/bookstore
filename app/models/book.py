from pydantic import BaseModel
from author import Author


class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: int
