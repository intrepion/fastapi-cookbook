from fastapi import FastAPI
from models import Book
from pydantic import BaseModel


class BookResponse(BaseModel):
    title: str
    author: str


app = FastAPI()


@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        },
    ]


@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {"author_id": author_id, "name": "Ernest Hemingway"}


@app.post("/book")
async def create_book(book: Book):
    return book


@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {"year": year, "books": ["Book 1", "Book 2"]}
    return {"books": ["All Books"]}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
    }
