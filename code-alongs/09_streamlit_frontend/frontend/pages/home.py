import streamlit as st
from pathlib import Path

book_path = Path(__file__).resolve().parents[2] / "assets" / "fastapi_book.png"
st.image(book_path)

st.markdown("# Bookies App")
