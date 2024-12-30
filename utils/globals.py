from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Path and File Names
db_path = "db"
pdf_files = [
    "pdfs/dscsa.pdf",
    "pdfs/DSCSADispenserGuide.pdf",
    "pdfs/EPCIS.pdf",
    "pdfs/GS1UserGuide.pdf",
]

# LangChaing Global Variables
embedding = FastEmbedEmbeddings()
