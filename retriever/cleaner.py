# -----------------------------------------
# Function: clean_documents
# Purpose:
#     Remove non-clinical pages before chunking.
#
# Input:
#     List[Document] : documents
#
# Returns:
#     List[Document] : cleaned_documents
# -----------------------------------------

REMOVE_PATTERNS = [
    "subject to copyright",
    "suggested citation",
    "electronic documents",
    "doi.org",
]


def clean_documents(documents):

    cleaned_documents = []

    for document in documents:

        text = document.page_content.lower()

        if any(pattern in text for pattern in REMOVE_PATTERNS):
            continue

        cleaned_documents.append(document)

    print(f"Removed {len(documents) - len(cleaned_documents)} non-clinical pages.")

    return cleaned_documents