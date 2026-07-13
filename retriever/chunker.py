from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


# -----------------------------------------
# Function: chunk_documents
# Purpose:
#     Split loaded documents into overlapping chunks.
#
# Input:
#     List[Document] : documents
#
# Returns:
#     List[Document] : chunks
# -----------------------------------------
def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks