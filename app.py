import streamlit as st
from markitdown import MarkItDown
import tempfile
import os

st.set_page_config(page_title="PDF to Markdown Converter", layout="wide")

st.title("PDF to Markdown Converter")
st.caption("100% local • No internet • No token limits")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        with st.spinner("Converting..."):
            md = MarkItDown()
            result = md.convert(tmp_file_path)
            markdown_content = result.text_content

        st.subheader("Preview")
        st.text_area("Markdown Output", markdown_content, height=400)
        
        st.download_button(
            label="Download Markdown",
            data=markdown_content,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
            mime="text/markdown"
        )
    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")
    finally:
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
