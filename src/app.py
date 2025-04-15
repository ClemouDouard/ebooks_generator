import streamlit as st

from main import run_1

"""
# Ebook generator
"""

topic = st.text_input("What is the topic of your book?")

if st.button("Generate"):
    run_1(topic)