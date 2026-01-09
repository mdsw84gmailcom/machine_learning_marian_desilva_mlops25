import streamlit as st
import httpx

# get all book data
all_books = httpx.get("http://127.0.0.1:8000/books").json()

# use list comprehension to list out all book titles
all_title = [book.get("title") for book in all_books]

st.markdown("# BookFinder")

selected_title = st.selectbox("Choose a title", options=all_title)

# get the selected book data
selected_book = httpx.get(
    f"http://127.0.0.1:8000/books/title/" + selected_title
).json()[0]

st.markdown(f"Author: {selected_book.get('author')}")
st.markdown(f"Title: {selected_book.get('title')}")
st.markdown(f"Publish year: {selected_book.get('year')}")
