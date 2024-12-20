from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
import utils.globals as globals


def get_model():
    cached_llm = Ollama(model="llama3.2")

    print("Loading Vector Store")
    vector_store = Chroma(
        persist_directory=globals.db_path, embedding_function=globals.embedding
    )
    print("Creating Retriever")
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 20, "score_threshold": 0.1},
    )
    raw_prompt = PromptTemplate.from_template(
        """
        <s>[INST] You are a assistant about the DSCSA law from FDA about RX Products. If you do not have an answer from the provided information, say so.[/INST] </s>
        [INST]  {input}
                Context: {context}
                Answer: 
        [/INST]
    """
    )
    print("Creating Document Chain")
    document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
    print("Creating Final Chain")
    chain = create_retrieval_chain(retriever, document_chain)
    return chain
