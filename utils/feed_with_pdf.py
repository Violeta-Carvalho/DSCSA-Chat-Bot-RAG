from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores import Chroma
import globals as globals

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, chunk_overlap=100, length_function=len, is_separator_regex=False
)


def feed_with_pdfs():
    loader = PDFPlumberLoader(globals.pdf_file)
    docs = loader.load_and_split()
    chunks = text_splitter.split_documents(docs)
    Chroma.from_documents(
        documents=chunks, embedding=globals.embedding, persist_directory=globals.db_path
    )


feed_with_pdfs()
