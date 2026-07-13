from langchain_community.document_loaders import PyPDFLoader

from config import PDF_PATH


# -----------------------------------------
# Function: load_pdf
# Purpose:
#     Load the guideline PDF into LangChain Documents.
#
# Input:
#     None
#
# Returns:
#     List[Document] : documents
# -----------------------------------------
def load_pdf():

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    return documents