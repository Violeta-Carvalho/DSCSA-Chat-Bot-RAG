import streamlit as st
from utils.model import get_model

st.title("DSCSA Bot")

chain = get_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Do you need any help with DCDSA?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    typing_placeholder = st.empty()
    typing_placeholder.markdown("**DSCSA Bot is typing...**")

    response = chain.invoke({"input": prompt})

    typing_placeholder.empty()

    with st.chat_message("assistant"):
        st.markdown(response["answer"])

    st.session_state.messages.append(
        {"role": "assistant", "content": response["answer"]}
    )
