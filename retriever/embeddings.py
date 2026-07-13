from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


# -----------------------------------------
# Function: load_embeddings
# Purpose:
#     Load the embedding model used for vector generation.
#
# Input:
#     None
#
# Returns:
#     HuggingFaceEmbeddings : embeddings
# -----------------------------------------
def load_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    print("Embedding model loaded.")

    return embeddings