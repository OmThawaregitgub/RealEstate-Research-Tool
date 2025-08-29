import pathlib
from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
# Use ChatOllama for the local model

# load_dotenv()

CHUNK_SIZE = 100
# It is the model that we use for word embedding.
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
# Initilizr directory path.
VECTORSTORE_DIR = "resources/vectorstore"
# We store our vector database in that dieractory.
COLLECTION_NAME = "real_estate"

llm = None
vector_store = None
def initialize_components():
    global llm, vector_store
    # Avoide reinitilization of ChatGroq constructor.
    if(llm is None):
        llm = ChatOllama(model="llama3", temperature=0.9,max_tokens=1000)
    if(vector_store is None):
        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            # Remove this line temporarily
            # persist_directory=VECTORSTORE_DIR,
            embedding_function=HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            )
        )
        print(vector_store)


def generate_answer(question):
    # It take the question as an input and return the answer.

    if(vector_store is None):
        raise RuntimeError("Vector store is not initialized")

    # The retriever convert the question into embedding.
    chain = RetrievalQAWithSourcesChain.from_llm(llm, retriever=vector_store.as_retriever())
    # Pull the revalent answer.
    result = chain({"question": question},return_only_outputs=True)
    sources = result.get("sources","")
    return result["answer"],sources


def process_urls(urls):
    """
    The function taker url as an input
    and return or scrap the data from that url and store it in a vector DB.
    """
    print("Initilize the vector database .....")
    initialize_components()
    # Reset your database.
    vector_store.reset_collection()

    print("Load data ...")
    loaders = SeleniumURLLoader(urls)
    data = loaders.load()
    print(data)
    print(vector_store)
    print("Splite text....")
    text_splitter = RecursiveCharacterTextSplitter(
        separators =["\n\n", "\n", " ", ""],
        chunk_size=CHUNK_SIZE, # The data id divide in that chunks.
        chunk_overlap=20
    )

    # Splite the text into small small chunks.
    texts = text_splitter.split_documents(data)

    print("Initilize the ID..........")
    #Create unique id's and store it into database.
    uuids = [str(uuid4()) for _ in range(len(texts))]
    # Convert the data into vector and store it into the vectore database.

    print("Add document start ...")
    try:
        print("Add document start ...")
        # Add the contant in vector database.
        print(vector_store.add_documents(texts, ids=uuids))
        print("Add document end ...")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Add document end ...")

if __name__ == "__main__":
    urls = [
            "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
            "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
            ]

    process_urls(urls)

    answer,source = generate_answer("Americans waiting for mortgage rates?")
    print(answer)
    print(source)