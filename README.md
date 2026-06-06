# PDF to Markdown Converter
<img width="1838" height="616" alt="image" src="https://github.com/user-attachments/assets/c338dd32-f04d-4a8c-8f70-6dd23019bb89" />

A simple, 100% local, offline single-page Streamlit web application that converts PDF files to Markdown using the [markitdown](https://github.com/microsoft/markitdown) library.

## Features
- **Local & Offline:** No internet required, no data leaves your machine, and no token limits.
- **Drag-and-Drop:** Easily upload your PDF files.
- **Live Preview:** View the converted markdown in a scrollable text area.
- **Download:** Save the converted markdown as a `.md` file with one click.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OumaySouissi/pdf-to-markdown-converter.git
   cd pdf-to-markdown-converter
   ```

2. **Install dependencies:**
   Ensure you have Python installed. It is recommended to use a virtual environment. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application locally:

```bash
streamlit run app.py
```

The application will open in your default web browser automatically.

## Built With
- [Streamlit](https://streamlit.io/) - The web framework used.
- [MarkItDown](https://github.com/microsoft/markitdown) - The underlying engine for converting PDF to Markdown.
