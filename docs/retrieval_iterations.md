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

### Change Made

### Files Modified

### Result

### Conclusion

### Next Iteration