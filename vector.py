from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

class PineconeVectorDB:
    
    def __init__(self, api_key,embedding): 
        self.db = Pinecone(api_key=api_key)
        self.embedding = embedding

    # creates an index of given name in the PineconeDB
    def create_index(self, index_name):
        self.db.create_index(
            name=index_name,
            dimension=3072,
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

    # loads, splits and stores the into the index created above
    def init_pineconedb_with_docs(self, filename, index):
        context_docs = self._split_and_index_source_documet(filename)
        PineconeVectorStore.from_documents(context_docs, self.embedding, index_name=index)

    # Loads and splits the data into chunks
    def _split_and_index_source_documet(self, filename):
        docs = TextLoader(filename).load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(docs)
        
    # Returns the vectorstore for retrieving
    def get_vectore_store(self, index):
        return PineconeVectorStore(
        index_name=index, embedding=self.embedding)