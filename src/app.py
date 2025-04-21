import streamlit as st

from main import run_1

print("#### STARTING ####")

if 'modified_content' not in st.session_state:
    st.session_state.modified_content = ""

print("#### STARTED ####")

"""
# Ebook generator
"""

topic = st.text_input("What is the topic of your book?")

if st.button("Generate"):
    print("#### GENERATING ####")
    with st.spinner("Generating..."):
        struct = run_1(topic)
    st.session_state.modified_content = struct.raw

if st.session_state.modified_content != "":
    with st.form(key="form", enter_to_submit=True):
        st.markdown(st.session_state.modified_content)
        st.session_state.modified_content = st.text_area("Modify the content:", value=st.session_state.modified_content, height=300)
        if st.form_submit_button("Generate Chapters"):
            st.markdown(st.session_state.modified_content) 