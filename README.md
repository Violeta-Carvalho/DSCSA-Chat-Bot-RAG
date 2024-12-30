# DSCSA AI

This is a Chat Bot made with the RAG (Retrieval-Augmented Generation) technique. It was built on Llama 3.2, and with a PDF describing the DSCSA. It is a PoC for creating an LLM which explains and describes the details of the DSCSA law, and how it applies GS1 concepts. It contains the Chat Bot page, and a page with the files it was built with. 

# Installation

To install this repository, you need to have [Ollama](https://ollama.com/) installed. If you have Linux, you can do so with the following command:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Then, you need to download Llama, and the necessary Python libraries.

```
ollama pull llama3.2
pip install -r requirements.txt
```

# Adding Documents to AI

To add new documents to the AI, you just need to add the PDF under `pdfs` folder, and then, on `utils/globals.py`, add the file path as `"pdfs/<FILE NAME>"` into the `pdf_files` variable. Finally, all you need to do is run:

```
python utils/feed_with_pdf.py
```

# Running

To run it, you need Ollama running in one terminal:

```
ollama serve
```

Then, run Streamlit in another one:

```
streamlit run Home.py
```
