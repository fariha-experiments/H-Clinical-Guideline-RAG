# H-Clinical-Guideline-RAG
Reads a clinical pdf, splits it , embeds it, chunks it, concatenates the chunks and feeds it to llm to get the most semantic answer


# 🩺 Clinical Guideline RAG

A Retrieval-Augmented Generation (RAG) application that enables semantic search over clinical guidelines using embeddings, vector databases, and a Large Language Model (LLM).

Built as part of my transition into AI Engineering with a focus on HealthTech.

---

## 🚀 Project Overview

Healthcare guidelines often span hundreds of pages, making it difficult to quickly locate relevant evidence.

This project demonstrates how Retrieval-Augmented Generation (RAG) can retrieve the most relevant sections of a clinical guideline and use an LLM to generate context-aware responses grounded in the source document.

The current implementation uses the **2023 International Evidence-Based Guideline for PCOS** as the knowledge base.

---

## 🛠️ Tech Stack

* Python
* Google Colab
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Google Gemini
* PyPDF

---

## 🔄 RAG Pipeline

1. Load the clinical guideline PDF.
2. Split the document into chunks.
3. Convert each chunk into vector embeddings.
4. Store embeddings in ChromaDB.
5. Embed the user's question.
6. Retrieve the most relevant chunks using semantic similarity search.
7. Pass the retrieved context to Gemini.
8. Generate a grounded response.

---

## 📂 Repository Structure

```text
clinical-guideline-rag/

├── notebook.ipynb
├── README.md
└── assets/
```

---

## 💡 Example Questions

* What are the Rotterdam criteria for PCOS?
* What are the symptoms of PCOS?
* How is hyperandrogenism diagnosed?
* What lifestyle interventions are recommended?
* What are the diagnostic criteria for adolescents?

---

## 📚 Key Concepts Learned

During this project I explored:

* Retrieval-Augmented Generation (RAG)
* Embeddings
* Semantic Search
* Vector Databases
* Chunking Strategies
* Similarity Search
* Prompt Engineering
* Retrieval Debugging

---

## 🔍 Retrieval Debugging

An important part of this project was evaluating retrieval quality rather than assuming the first results were correct.

Experiments included:

* Inspecting retrieved chunks
* Evaluating ranking quality
* Understanding chunking effects
* Analyzing retrieval failures
* Comparing semantic matches with expected results

---

## 🚧 Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Metadata-aware retrieval
* Reranking
* Citation support
* Multi-document retrieval
* Evaluation framework
* Streamlit interface
* Docker deployment

---

## 🎯 Purpose

This project is part of my AI Engineering portfolio and documents my journey from building a basic RAG pipeline to developing production-minded AI systems for healthcare applications.
