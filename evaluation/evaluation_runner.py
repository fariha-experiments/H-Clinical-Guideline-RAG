import pandas as pd


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

#v2 def retrieve_top_k_chunks(question):
#v2   print(question)
    #logiv goes here: similarity_search model is called?

#loops through benchmark to load queries and feeds each query to retreiver 
def run_benchmark(benchmark_df):
    for index, row in benchmark_df.iterrows():
        query_question = row["user_question"]
        print(query_question)
        #retreived_chunks = retrieve_top_k_chunks(query_question)

    #prepare the df to feed save_results    
  

#def save_results(retreived_df):

def main():

    benchmark_df = load_benchmark()

    print(f"Loaded {len(benchmark_df)} benchmark queries.\n")

    run_benchmark(benchmark_df)

    # V2:
    # retrieved_df = run_benchmark(benchmark_df)

    # V3:
    # save_results(retrieved_df)


if __name__ == "__main__":
    main()
 