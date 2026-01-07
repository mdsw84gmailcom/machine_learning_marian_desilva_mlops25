from fastapi import FastAPI
from data_processing import library_data, Book

# list of elements that are pydantic model
books: list[Book] = library_data("library.json").books

app = FastAPI()


@app.get("/books")
async def read_books():
    # can return a pydantic model because
    # fastapi serializes it to json under the hood
    return books


# path parameter
@app.get("/book/{id}")
async def read_book_by_id(id: int):
    return [book for book in books if book.id == id]
