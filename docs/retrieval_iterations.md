# Retrieval Iterations

## Clinical Guideline RAG

## Baseline (Iteration 0)

### Objective
Build a working retrieval pipeline.

### Benchmark
- 6 benchmark questions
- Top-K = 3
- Embedding: BAAI/bge-small-en-v1.5
- Chunk Size: 800
- Overlap: 100

### Observations

#### Good
- Diagnostic criteria retrieved relevant pages.
- Strong semantic matches for several queries.

#### Issues Found
1. Document Processing
   - Headers, copyright pages and formatting noise retrieved.

2. Chunking
   - Some chunks start/end mid-topic.

3. Ranking
   - General answers occasionally ranked below specific ones.

4. Semantic Retrieval
   - Some concept mismatches.

### Decision

Highest-impact issue:
Document Processing

Next Experiment:
Clean extracted text before chunking.
- ...

### Evidence
- Query: "What are the diagnostic criteria for PCOS?"
  - Rank 2 should arguably be Rank 1.
- Query: "What are the known causes of PCOS?"
  - Retrieved copyright page instead of relevant content.

### Next Iteration
Remove document noise before chunking.

---

## Iteration 1 - Document Cleaning

### Goal

Determine whether removing non-clinical metadata from the document improves retrieval quality.

### Problem

Initial retrieval results included irrelevant copyright and document metadata from the source PDF.

### Change Made

Added a document-cleaning step that identifies predefined non-clinical metadata patterns and removes the affected content before chunking.

### Files Modified

- `retriever/cleaner.py`

### Result

The previously identified metadata/copyright content no longer appeared in the retrieval results.

However, irrelevant retrieval remained in some benchmark domains, particularly symptoms and causes.

### Conclusion

Document cleaning successfully addressed the identified metadata contamination problem, but did not resolve the broader retrieval-quality issues.

### Next Iteration

Investigate the remaining retrieval failures and determine whether they are primarily caused by chunking, retrieval, or ranking.

------------