Evaluation Playbook v1
Purpose

This document captures how we evaluate retrieval systems, what observations to record, and how our evaluation methodology evolves over iterations.

The goal is not only to determine whether retrieval is good or bad, but to understand why a retrieval succeeded or failed and what engineering change should be tested next.

Evaluation Mindset

Do not ask:

Is this retrieval good?

Instead ask:

Why did the retriever think this chunk was relevant?


Every failure should suggest a future experiment.

## Evaluation Process

For each benchmark question:

1. Read the question.
2. Read the Top-K retrieved chunks.
3. Ask:
   - Is the answer present?
   - Is it ranked correctly?
   - Is the chunk readable?
4. Categorize the issue.
5. Suggest one improvement.

Retrieval Evaluation Playbook v1
Evaluation Template
Query
What are the diagnostic criteria for PCOS?
Overall Verdict
✅ Good
⚠️ Partial
❌ Poor

Short summary (1-2 lines).

Findings

Each finding belongs to one primary category.

Finding 1
Category

Ranking Issue

Sub-Issues
More relevant chunk retrieved at lower rank.
Specialized content ranked above foundational content.
Duplicate semantic matches competing for Rank 1.
Evidence
Page 63 (AMH) ranked above Page 60 (Ultrasound Criteria).
The general diagnostic criteria would better answer the query.
Suggested Experiment
Test reranking.
Compare different embedding models.
Finding 2
Category

Chunking Issue

Sub-Issues
Chunk starts mid-sentence.
Heading separated from content.
Important context split across chunk boundary.
Evidence
Retrieved chunk begins after the ultrasound heading.
Reader loses the subject immediately.
Suggested Experiment
Increase overlap.
Try heading-aware chunking.
Finding 3
Category

Document Parsing Issue

Sub-Issues
Page headers included.
Footer noise.
Formatting artifacts.
Evidence
Chunk contains guideline title instead of content.
Suggested Experiment
Clean headers/footers before embedding.
Suggested Categories

# Retrieval Evaluation Categories

## 1. Retrieval

### Ranking
- Better chunk retrieved at a lower rank
- Correct information not in Top-1
- Reranking could improve ordering

### Semantic Match
- Retrieved chunk is related but doesn't answer the intent
- Retrieves only one aspect of the answer
- Topic overlap without answering the question

### Duplicate Results
- Nearly identical chunks retrieved multiple times
- Low diversity in Top-K results

---

## 2. Chunking

### Boundary Issues
- Chunk starts mid-sentence
- Chunk ends abruptly
- Heading separated from content

### Missing Context
- Important surrounding information excluded
- Definition split across chunks

### Chunk Size
- Chunk too small
- Chunk too large
- Too much irrelevant context

---

## 3. Document Processing

### Parsing
- Header/footer retrieved
- Table of contents retrieved
- References instead of content

### Formatting Noise
- Page numbers
- Broken PDF formatting
- Repeated guideline titles

### OCR (Future)
- Incorrect extracted text
- Missing words
- Garbled characters

---

## 4. Corpus

### Corpus Coverage
- Information doesn't exist in the document

### Out of Scope
- Question cannot be answered from this corpus

### Missing Information
- Guideline intentionally doesn't discuss the topic

---

## 5. Benchmark

### Ambiguous Question
- Multiple interpretations
- Too broad

### Synonym Gap
- Query wording differs from guideline terminology

### Unrealistic Query
- Not representative of real user searches

### Typo / Grammar
- Spelling mistakes
- Broken query

---

## 6. Embeddings

### Weak Semantic Match
- Similar meaning missed
- Incorrect semantic neighbors retrieved

### Vocabulary Gap
- Medical terminology mismatch
- Acronyms or abbreviations not understood
