from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

class PineconeVectorDB:
    
    def __init__(self, api_key,embedding): 
        self.db = Pinecone(api_key=api_key)
        self.embedding = embedding

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

    def init_pineconedb_with_docs(self, filename, index):
        context_docs = self._split_and_index_source_documet(filename)
        PineconeVectorStore.from_documents(context_docs, self.embedding, index_name=index)

    def _split_and_index_source_documet(self, filename):
        docs = TextLoader(filename).load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(docs)
        
    def get_vectore_store(self, index):
        return PineconeVectorStore(
        index_name=index, embedding=self.embedding)