from langchain_community.vectorstores import Chroma

from retriever.loader import load_pdf
from retriever.chunker import chunk_documents
from retriever.embeddings import load_embeddings

from config import COLLECTION_NAME


# -----------------------------------------
# Purpose:
#     Create a Chroma vector database from the PDF chunks.
#
# Input:
#     None
#
# Returns:
#     Chroma : db
# -----------------------------------------
def build_vector_store():

    documents = load_pdf()

    chunks = chunk_documents(documents)

    embeddings = load_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME
    )

    return db

#--------- temp test | delete in revision--------------
if __name__ == "__main__":

    db = build_vector_store()

    print(f"vector here{type(db)}")
    print(db)