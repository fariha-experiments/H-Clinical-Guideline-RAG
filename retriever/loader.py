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


# ----------temp ----------------
if __name__ == "__main__":
    documents = load_pdf()

    print("\n========== PAGE 1 ==========\n")
    print(documents[0].page_content)

    print("\n========== PAGE 60 ==========\n")
    print(documents[59].page_content)