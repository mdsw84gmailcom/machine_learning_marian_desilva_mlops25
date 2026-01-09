import streamlit as st
import httpx
import pandas as pd

data = httpx.get("http://127.0.0.1:8000/books").json()
df = pd.DataFrame(data)

st.markdown("# Books dashboard")
