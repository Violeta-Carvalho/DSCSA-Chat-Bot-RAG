from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
import utils.globals as globals


def get_model():
    cached_llm = Ollama(model="llama3.2")

    vector_store = Chroma(
        persist_directory=globals.db_path, embedding_function=globals.embedding
    )
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 5, "score_threshold": 0.3},
    )
    raw_prompt = PromptTemplate.from_template(
        """
            <s>[INST] You are a friendly and knowledgeable assistant. Use the following context and chat history to provide accurate and engaging responses to the user's queries. 
            If you cannot answer based on the provided context, politely inform the user. Keep your tone professional but conversational.
            The user did not send you the context, nor the chat history, do not talk to them about the context.
            You do not need to constantly readdress messages in the chat history as if they were sent a long time ago, they are all recent.
            [/INST]</s>
            [INST]  
            Context: {context}
            Chat History: {history}
            User Input: {input}
            Answer: 
            [/INST]
        """
    )

    document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
    chain = create_retrieval_chain(retriever, document_chain)
    return chain
