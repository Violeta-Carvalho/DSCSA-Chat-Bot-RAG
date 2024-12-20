from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Path and File Names
db_path = "db"
pdf_file = "pdfs/dscsa.pdf"

# LangChaing Global Variables
embedding = FastEmbedEmbeddings()
