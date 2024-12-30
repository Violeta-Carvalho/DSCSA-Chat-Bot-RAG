import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import utils.globals as globals

st.title("PDF Files")
st.write("Below are all the files that the Bot is using.")

for pdf_file in globals.pdf_files:
    st.subheader(pdf_file)

    if dscsa_button := st.button("View File", key=pdf_file + "view"):
        close_dscsa_button = st.button("Close", key=pdf_file + "close")
        if dscsa_button and not close_dscsa_button:
            pdf_viewer(pdf_file, key=pdf_file)
