# Retrieval Iterations

## Clinical Guideline RAG

## Baseline (Iteration 0)

### Objective
Build a working retrieval pipeline.

### Benchmark
- 6 benchmark questions
- Top-K = 3
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

## Iteration 2 - Retrieval Score Diagnostics

### Goal
Inspect retrieval scores to understand retrieval behaviour.

### Problem
Retrieved chunks were sometimes semantically related but not the most relevant evidence.

### Hypothesis
Retrieval scores will help identify whether poor results are caused by weak similarity or by retrieval selecting the wrong semantically similar chunks.

### Change Made
Changed `similarity_search()` to `similarity_search_with_score()` and added `retrieval_score` to the evaluation output.

### Files Modified
`evaluation_runner.py`

### Result
Scores were successfully captured for all 18 retrieval results.

The scores show that lower-scoring chunks are closer to the query, but a stronger score does not guarantee that the chunk contains the correct clinical evidence.

### Conclusion
Score visibility helps diagnose retrieval behaviour, but score alone cannot determine retrieval correctness.

### Next Iteration
Experiment with chunking strategy and evaluate whether better chunk context improves Top-K retrieval.

-----------

## Iteration 3 - Chunk Size Experiment

### Goal

Evaluate whether increasing chunk size improves retrieval of relevant clinical evidence.

### Problem

Retrieved chunks were sometimes semantically related to the query but did not contain the most relevant clinical evidence.

### Hypothesis

Larger chunks may preserve more surrounding clinical context and improve Top-K retrieval relevance.

### Change Made

Increased chunk_size from 800 to 1200 while keeping the chunking method, chunk overlap, embedding model, vector database, benchmark queries, and TOP_K unchanged.

### Files Modified

config.py

### Result

The 1200-token chunks did not materially resolve the retrieval failures.

Diagnostic queries continued to retrieve semantically related but clinically incorrect or incomplete evidence. For example, diagnostic queries continued to retrieve AMH and ultrasound content rather than the Rotterdam diagnostic criteria, while symptom and cause queries also returned broader guideline or unrelated sections.

### Conclusion

Increasing chunk size did not materially improve retrieval quality. Chunk size does not appear to be the primary retrieval bottleneck in the current pipeline.

### Next Iteration

Compare the current embedding model with a retrieval-oriented embedding model while keeping the corpus, chunking, benchmark, vector database, and retrieval configuration unchanged.