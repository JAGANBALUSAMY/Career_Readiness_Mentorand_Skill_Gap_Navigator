"""RAG Vector Store for Resume Database."""
import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from typing import List, Dict
import os


class ResumeVectorStore:
    """Vector database for storing and retrieving resume information."""

    def __init__(self):
        """Initialize vector store with ChromaDB."""

        # 🔥 Replaced Google embeddings with FREE HuggingFace embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.collection_name = "resumes"
        self.persist_directory = "./data/chroma_db"

        # Ensure directory exists
        os.makedirs(self.persist_directory, exist_ok=True)

        self.vectorstore = None
        self._initialize_vectorstore()

    def _initialize_vectorstore(self):
        """Initialize or load existing vector store."""
        try:
            self.vectorstore = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )
        except Exception as e:
            print(f"Vector store init warning (creating new): {e}")
            self.vectorstore = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )

    def add_resume(self, resume_text: str, metadata: Dict):
        """Add resume to vector database."""

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        )

        chunks = text_splitter.create_documents(
            [resume_text],
            metadatas=[metadata]
        )

        self.vectorstore.add_documents(chunks)

        if hasattr(self.vectorstore, 'persist'):
            self.vectorstore.persist()

    def search_similar_resumes(self, query: str, k: int = 3) -> List[Dict]:
        """Search for similar resume sections."""
        if not self.vectorstore:
            return []

        results = self.vectorstore.similarity_search_with_score(query, k=k)

        return [
            {
                'content': doc.page_content,
                'metadata': doc.metadata,
                'score': score
            }
            for doc, score in results
        ]

    def get_relevant_context(self, job_description: str, k: int = 5) -> str:
        """Get relevant resume context for a job description."""
        results = self.search_similar_resumes(job_description, k=k)

        if not results:
            return ""

        context = "\n\n---\n\n".join([
            f"**Similar Resume Section:**\n{r['content']}"
            for r in results
        ])

        return context
