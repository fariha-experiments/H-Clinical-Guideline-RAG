import pandas as pd

from retriever.vector_db import build_vector_store

from config import TOP_K


#constants section
BENCHMARK_FILE = "data/benchmark_queries.csv"
OUTPUT_FILE = "data/retrieval_results.csv"
TOP_K = 3


#loading files section
#Responsibility:
#Read benchmark csv 
#Return DataFrame
def load_benchmark():
    queries = pd.read_csv(BENCHMARK_FILE)
    return queries


# -----------------------------------------
# Function: retrieve_top_k_chunks
# Purpose:
#     Retrieve Top-K relevant chunks for a query.
#
# Input:
#     Chroma : db
#     String : question
#
# Returns:
#     List : retrieved_chunks
# -----------------------------------------

def retrieve_top_k_chunks(db, question):

    retrieved_chunks = db.similarity_search(
        question,
        k=TOP_K
    )

    return retrieved_chunks

# -----------------------------------------
#loops through benchmark to load queries and feeds each query to retreiver 
# Purpose:
#     Loop through benchmark questions and
#     retrieve Top-K chunks.
#
# Input:
#     None
#
# Returns:
#     None
# -----------------------------------------
def run_benchmark(benchmark_df):
    # Build vector database
    db = build_vector_store()

    results=[]

    for index, row in benchmark_df.iterrows():
        question = row["user_question"]
        
        retrieved_chunks = retrieve_top_k_chunks(
            db,
            question
        )

    #debug stage 1    print("\n===================================")
     #   print(f"Question: {question}")

        #for rank, chunk in enumerate(retrieved_chunks, start=1):

       #     print(f"\nResult {rank}")
            

    #prepare the df to feed save_results 

        for rank, chunk in enumerate(retrieved_chunks, start=1):

            results.append({

                "query_id": row["query_id"],
                "category": row["category"],
                "difficulty": row["difficulty"],
                "question": question,

                "retrieval_rank": rank,

                "retrieved_page": chunk.metadata.get("page"),

                "retrieved_chunk": chunk.page_content

            })

    return results   
  

#def save_results(retreived_df):
# -----------------------------------------
# Function: save_results
# Purpose:
#     Save retrieval results to CSV.
#
# Input:
#     List : results
#
# Returns:
#     None
# -----------------------------------------
def save_results(results):

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"\nSaved {len(results_df)} retrieval results.")


def main():

    benchmark_df = load_benchmark()

    print(f"Loaded {len(benchmark_df)} benchmark queries.\n")

    results = run_benchmark(
        benchmark_df
    )

    save_results(results)

    # V2:
    # retrieved_df = run_benchmark(benchmark_df)

    # V3:
    # save_results(retrieved_df)


if __name__ == "__main__":
    main()
 