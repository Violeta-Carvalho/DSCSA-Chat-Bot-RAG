import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import utils.globals as globals

st.title("PDF Files")
st.write("Below are all the files that the Bot is using.")

st.subheader("DSCSA File")

if dscsa_button := st.button("View File"):
    close_dscsa_button = st.button("Close")
    if dscsa_button and not close_dscsa_button:
        pdf_viewer(globals.pdf_file)
