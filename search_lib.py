from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.csv_loader import CSVLoader
from st_files_connection import FilesConnection
#from mylib import BedrockEmbeddings
import streamlit as st


aws_credentials = {
    "aws_access_key_id": st.secrets["aws"]["access_key_id"],
    "aws_secret_access_key": st.secrets["aws"]["secret_access_key"],
    "region_name": st.secrets["aws"]["region"]
}


def get_index(): #creates and returns an in-memory vector store to be used in the application
    
    embeddings = BedrockEmbeddings() #create a Titan Embeddings client
    
    loader = CSVLoader(file_path="fashion_faqs.csv")
    conn = st.connection('s3', type=FilesConnection)
    documents = loader.load()

    index_creator = VectorstoreIndexCreator(
        vectorstore_cls=FAISS,
        embedding=embeddings,
        text_splitter=CharacterTextSplitter(chunk_size=300, chunk_overlap=0),
    )

    index_from_loader = index_creator.from_loaders([loader])
    
    return index_from_loader
    

def get_similarity_search_results(index, question):
    results = index.vectorstore.similarity_search_with_score(question)
    
    flattened_results = [{"content":res[0].page_content, "score":res[1]} for res in results] #flatten results for easier display and handling
    
    return flattened_results
