from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores import Chroma
import globals as globals


def feed_with_pdfs():
    for pdf_file in globals.pdf_files:
        loader = PDFPlumberLoader(pdf_file)
        docs = loader.load_and_split()
        chunk_size = len(docs) * 10
        chunk_overlap = round(chunk_size / 4)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
        chunks = text_splitter.split_documents(docs)
        Chroma.from_documents(
            documents=chunks,
            embedding=globals.embedding,
            persist_directory=globals.db_path,
        )


feed_with_pdfs()
