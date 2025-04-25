from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
def setup_vector_db(doc_path):
  loader = TextLoader(doc_path)
  documents = loader.load()
  embeddings = HuggingFaceEmbeddings()
  db = FAISS.from_documents(documents, embeddings)
  return db
