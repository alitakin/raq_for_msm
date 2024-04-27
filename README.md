# Semantic Search Example



This demonstrates a simple embeddings search application with Amazon Titan Embeddings, LangChain, and Streamlit.

The example matches a user’s query to the closest entries in an in-memory vector database. We then display those matches directly in the user interface. This can be useful if you want to troubleshoot a RAG application, or directly evaluate an embeddings model.

For simplicity, we use the in-memory [FAISS](https://github.com/facebookresearch/faiss) database to store and search for embeddings vectors. In a real-world scenario at scale, you will likely want to use a persistent data store like the vector engine for [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/serverless-vector-engine/) or the pgvector extension for PostgreSQL.



## Contents

The example consists of four files: A Streamlit application in Python, a supporting file to make calls to Bedrock, a requirements file, and a data file to search against.


## Setup 

From the command line, run the following in the code folder:

```
pip3 install -r requirements.txt -U
```

## Running

From the command line, run the following in the code folder:

```
streamlit run search_app.py
```

You should now be able to access the Streamlit web application from your browser.


## Try a few prompts from the web application:

#### Specific Item Inquiry
- "Tell me about dresses by Adidas."
- "Do you have shoes for women?"

#### Brand Focus
- "What products do you have from Zara?"
- "List all items made by H&M."

#### Category Specific
- "What do you have in men’s footwear?"
- "Can I find women's dresses?"

#### Combination Questions
- "I need information on Adidas products for men."
- "Are there any T-shirts available for kids?"

#### Edge Cases and Details
- "What materials are the T-shirts made of?"
- "Do the women's shoes come in different colors?"

#### Out of Scope
- "How do I return a product?"
- "What are the warranty conditions for footwear?"





