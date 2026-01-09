import streamlit as st
from pathlib import Path

book_path = Path(__file__).parents[2] / "assets" / "fastapi_book.png"

st.markdown("# Bookies App")

st.image(book_path)
