from fastapi import FastAPI
from data_processing import library_data, Book

# list of elements that are pydantic model
books: list[Book] = library_data("library.json").books

app = FastAPI()


# ----------- READ ---------------------


@app.get("/books")
async def read_books():
    # can return a pydantic model because
    # fastapi serializes it to json under the hood
    return books


# path parameter
@app.get("/book/{id}")
async def read_book_by_id(id: int):
    return [book for book in books if book.id == id]


# ------------------ CREATE ---------------


@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)

    books.append(new_book)
    return new_book


# -------------------- UPDATE --------------


@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] = updated_book

    return updated_book


# -------------------- DELETE -------------


@app.delete("/books/delete_book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            break
