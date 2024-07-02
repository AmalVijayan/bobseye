from langchain_openai import OpenAIEmbeddings
from linter import AILinter
from vector import PineconeVectorDB
import argparse
import os

index_name = os.environ['PINECONE_INDEX_NAME']
sourcefile = os.environ['DATA_SOURCE_FILE_NAME']
embedding = OpenAIEmbeddings(model=os.environ['OPENAI_EMBEDDING_MODEL'])
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']

def main():
    parser = argparse.ArgumentParser(description="Creates a vectorDB with rules and lints a code snippet based on arguments passed")
    parser.add_argument("function", 
                        choices=['build_vector_db', 'lint_code'])
    args = parser.parse_args()

    if args.function == 'build_vector_db':
        build_vector_db()
    elif args.function == 'lint_code':
        lint_code()
    else:
        raise Exception('invalid argument!')

def build_vector_db():
    vector_db = PineconeVectorDB(PINECONE_API_KEY, embedding)
    vector_db.create_index(index_name)
    vector_db.init_pineconedb_with_docs(sourcefile, index_name)

def lint_code():
    inputs = get_inputs()
    vector_db = PineconeVectorDB(PINECONE_API_KEY, embedding)
    retriever = vector_db.get_vectore_store(index_name).as_retriever()
    linter = AILinter('gpt-4')
    linter.lint_code_snippets_with_rag(inputs, retriever)
    linter.write_results_to_file('lint-results.txt')

def get_inputs():
    unclean_code =  """
                    def c(a, b):
                        x = []
                        for i in range(len(a)):
                            x.append(a[i] + b[i])
                        return x
                    """
    
    clean_code = """
                 def add_elementwise(list1, list2):
                    if len(list1) != len(list2):
                        raise ValueError("Both lists must have the same length.")

                    return [x + y for x, y in zip(list1, list2)]
                 """
    return [
            unclean_code, 
            clean_code
            ]

if __name__ == '__main__':
    main()
    