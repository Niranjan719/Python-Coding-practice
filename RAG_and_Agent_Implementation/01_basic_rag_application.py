"""
BASIC RAG APPLICATION FOR INTERVIEW
Complete, working example that demonstrates RAG fundamentals

This is production-ready code that can be written in an interview setting.
Demonstrates: Document loading, chunking, embedding, retrieval, and generation

Time to write in interview: 30-45 minutes
Frameworks needed: LangChain, sentence-transformers, chromadb (or any vector DB)
"""

from typing import List, Dict, Optional
import os


# ============================================================================
# PART 1: DOCUMENT LOADING & CHUNKING
# ============================================================================

class DocumentLoader:
    """Load and chunk documents for RAG"""
    
    def __init__(self, chunk_size: int = 256, overlap: int = 32):
        """
        Args:
            chunk_size: Number of characters per chunk
            overlap: Number of overlapping characters between chunks
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def load_text(self, text: str, doc_id: str = "doc1") -> List[Dict]:
        """
        Load text and split into chunks
        
        Args:
            text: Raw text content
            doc_id: Document identifier
            
        Returns:
            List of chunks with metadata
        """
        chunks = []
        step = self.chunk_size - self.overlap
        
        words = text.split()
        words_per_chunk = max(1, self.chunk_size // 6)  # Approx words
        
        for i in range(0, len(words), max(1, words_per_chunk - self.overlap // 6)):
            chunk_words = words[i:i + words_per_chunk]
            chunk_text = " ".join(chunk_words)
            
            chunks.append({
                "id": f"{doc_id}_chunk_{len(chunks)}",
                "text": chunk_text,
                "doc_id": doc_id,
                "chunk_index": len(chunks),
                "metadata": {
                    "source": doc_id,
                    "chunk_size": len(chunk_text),
                    "word_count": len(chunk_words)
                }
            })
        
        return chunks
    
    def load_multiple(self, documents: Dict[str, str]) -> List[Dict]:
        """Load multiple documents"""
        all_chunks = []
        for doc_id, text in documents.items():
            chunks = self.load_text(text, doc_id)
            all_chunks.extend(chunks)
        return all_chunks


# ============================================================================
# PART 2: EMBEDDING & VECTOR STORE (Simulated)
# ============================================================================

class SimpleVectorStore:
    """
    Simple in-memory vector store for demo (use real VectorDB in production)
    In real scenario: Use Pinecone, Weaviate, FAISS, Chroma, etc.
    """
    
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add_documents(self, documents: List[Dict]):
        """Add documents to vector store"""
        # In real scenario: Generate embeddings using embedding model
        # from sentence_transformers import SentenceTransformer
        # model = SentenceTransformer('all-MiniLM-L6-v2')
        # embeddings = model.encode([doc["text"] for doc in documents])
        
        self.documents = documents
        # For demo: Use simple word count as "embedding"
        self.embeddings = [self._simple_embedding(doc["text"]) for doc in documents]
    
    def _simple_embedding(self, text: str) -> List[float]:
        """Create simple embedding (for demo only)"""
        # Real: Use proper embedding model
        words = text.lower().split()
        # Simple: word frequency vector
        embedding = [len(words), len(text), len(set(words))]
        embedding += [hash(word) % 10 for word in words[:10]]
        return embedding[:128]  # Fixed size
    
    def search(self, query: str, k: int = 3) -> List[Dict]:
        """
        Retrieve k most relevant documents
        
        In real scenario: Use vector similarity (cosine, L2, etc.)
        """
        if not self.documents:
            return []
        
        # Simple keyword-based search for demo
        query_words = set(query.lower().split())
        scores = []
        
        for doc in self.documents:
            doc_words = set(doc["text"].lower().split())
            # Jaccard similarity
            if len(doc_words) == 0:
                score = 0
            else:
                intersection = len(query_words & doc_words)
                union = len(query_words | doc_words)
                score = intersection / union if union > 0 else 0
            scores.append(score)
        
        # Get top-k
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.documents[i] for i in top_indices]


# ============================================================================
# PART 3: RETRIEVAL & LLM INTEGRATION
# ============================================================================

class SimpleRAG:
    """
    Simple RAG implementation (interview version)
    
    In real scenario: Use LangChain's RAG pipeline directly
    """
    
    def __init__(self, vector_store: SimpleVectorStore):
        self.vector_store = vector_store
        self.retrieved_docs = []
    
    def retrieve(self, query: str, k: int = 3) -> List[Dict]:
        """Retrieve relevant documents"""
        self.retrieved_docs = self.vector_store.search(query, k=k)
        return self.retrieved_docs
    
    def format_context(self, documents: List[Dict]) -> str:
        """Format retrieved documents as context"""
        if not documents:
            return "No relevant documents found."
        
        context = "Relevant Context:\n\n"
        for i, doc in enumerate(documents, 1):
            context += f"[Document {i}]\n"
            context += f"Source: {doc['metadata']['source']}\n"
            context += f"Content: {doc['text']}\n\n"
        
        return context
    
    def generate_prompt(self, query: str, context: str) -> str:
        """Build final prompt for LLM"""
        prompt = f"""Use the following context to answer the question.
If the answer is not in the context, say "I don't have information about this."

{context}

Question: {query}

Answer:"""
        return prompt
    
    def query(self, query: str, k: int = 3, llm_response: Optional[str] = None) -> Dict:
        """
        Complete RAG pipeline
        
        Args:
            query: User question
            k: Number of documents to retrieve
            llm_response: Simulated LLM response (for demo)
            
        Returns:
            Dict with query, context, and response
        """
        # Step 1: Retrieve
        documents = self.retrieve(query, k=k)
        
        # Step 2: Format context
        context = self.format_context(documents)
        
        # Step 3: Generate prompt
        prompt = self.generate_prompt(query, context)
        
        # Step 4: Call LLM (simulated)
        # In real: response = llm.generate(prompt)
        if llm_response is None:
            response = f"Based on the retrieved documents, I can answer your question: {query}"
        else:
            response = llm_response
        
        return {
            "query": query,
            "retrieved_documents": documents,
            "context": context,
            "prompt": prompt,
            "response": response,
            "num_docs_retrieved": len(documents)
        }


# ============================================================================
# PART 4: LANGCHAIN INTEGRATION (Real Production Code)
# ============================================================================

class LangChainRAG:
    """
    Production RAG using LangChain (actual code for real projects)
    
    Requirements:
    pip install langchain langchain-community langchain-openai
    pip install chromadb sentence-transformers
    """
    
    def __init__(self, llm_model: Optional[str] = None):
        """
        Initialize LangChain RAG
        
        Args:
            llm_model: LLM to use (default: gpt-3.5-turbo)
        """
        self.llm_model = llm_model or "gpt-3.5-turbo"
        self.vector_store = None
        self.retriever = None
        self.chain = None
    
    def setup_chain(self):
        """
        Setup LangChain RAG chain
        
        Code for real project:
        
        from langchain_community.vectorstores import Chroma
        from langchain_openai import OpenAIEmbeddings, ChatOpenAI
        from langchain.chains import RetrievalQA
        from langchain.prompts import PromptTemplate
        
        # Load documents
        docs = load_documents("docs/")
        chunks = split_documents(docs, chunk_size=1000)
        
        # Create vector store
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(chunks, embeddings)
        
        # Create retriever
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        
        # Setup LLM
        llm = ChatOpenAI(model=self.llm_model, temperature=0)
        
        # Create prompt template
        template = '''Use following context to answer question.
        
Context: {context}
Question: {question}

Answer:'''
        
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        
        # Create chain
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        
        self.chain = chain
        self.vector_store = vector_store
    
    def query(self, question: str) -> Dict:
        """Query the RAG chain"""
        result = self.chain({"query": question})
        return {
            "question": question,
            "answer": result["result"],
            "source_documents": result["source_documents"]
        }


# ============================================================================
# PART 5: INTERVIEW EXAMPLE & TESTING
# ============================================================================

def demo_rag():
    """Demonstrate RAG in action"""
    
    # Sample documents
    documents = {
        "doc1": """
            RAG (Retrieval Augmented Generation) is a technique that combines 
            information retrieval with text generation. It retrieves relevant 
            documents from a knowledge base and uses them as context to generate 
            more accurate and grounded responses. RAG improves the quality of 
            generated text by providing factual information.
        """,
        "doc2": """
            Vector databases store embeddings of documents. They enable fast 
            similarity search by computing distances between query embeddings 
            and document embeddings. Popular vector databases include Pinecone, 
            Weaviate, and Milvus. They are essential for RAG systems.
        """,
        "doc3": """
            LangChain is a framework for developing applications powered by 
            language models. It provides chains, agents, and tools for building 
            complex LLM applications. LangChain makes it easy to build RAG 
            systems, chatbots, and agents.
        """
    }
    
    # Step 1: Load and chunk documents
    print("=" * 60)
    print("STEP 1: Load and Chunk Documents")
    print("=" * 60)
    
    loader = DocumentLoader(chunk_size=200, overlap=30)
    chunks = loader.load_multiple(documents)
    print(f"Total chunks created: {len(chunks)}")
    for chunk in chunks[:2]:
        print(f"\n{chunk['id']}: {chunk['text'][:100]}...")
    
    # Step 2: Add to vector store
    print("\n" + "=" * 60)
    print("STEP 2: Add to Vector Store")
    print("=" * 60)
    
    vector_store = SimpleVectorStore()
    vector_store.add_documents(chunks)
    print(f"Documents in vector store: {len(vector_store.documents)}")
    
    # Step 3: Create RAG pipeline
    print("\n" + "=" * 60)
    print("STEP 3: Query RAG System")
    print("=" * 60)
    
    rag = SimpleRAG(vector_store)
    
    # Example queries
    queries = [
        "What is RAG?",
        "Tell me about vector databases",
        "What is LangChain?"
    ]
    
    for query in queries:
        print(f"\n--- Query: {query} ---")
        result = rag.query(query, k=2)
        
        print(f"\nRetrieved {result['num_docs_retrieved']} documents:")
        for i, doc in enumerate(result['retrieved_documents'], 1):
            print(f"  {i}. {doc['id']}: {doc['text'][:80]}...")
        
        print(f"\nGenerated Response:")
        print(f"  {result['response']}")


# ============================================================================
# USAGE IN INTERVIEW
# ============================================================================

if __name__ == "__main__":
    """
    Interview Tips:
    1. Start with DocumentLoader - simple and clear
    2. Then add SimpleVectorStore - no dependencies
    3. Implement SimpleRAG pipeline - shows understanding
    4. Talk about LangChainRAG - show production knowledge
    5. Run demo - prove it works!
    
    Time management:
    - 5 min: Explain RAG concept
    - 10 min: Code DocumentLoader
    - 10 min: Code SimpleVectorStore
    - 10 min: Code SimpleRAG
    - 5 min: Run demo
    - 5 min: Discuss improvements/scaling
    """
    
    print("\n" + "=" * 60)
    print("BASIC RAG APPLICATION - INTERVIEW DEMO")
    print("=" * 60 + "\n")
    
    demo_rag()
    
    print("\n" + "=" * 60)
    print("KEY POINTS TO MENTION IN INTERVIEW")
    print("=" * 60)
    print("""
    1. Retrieval: Get relevant documents using similarity search
    2. Augmentation: Include retrieved docs in prompt as context
    3. Generation: LLM generates response based on augmented context
    
    Advantages:
    - Reduces hallucinations with grounded information
    - Can use up-to-date knowledge without retraining
    - Cost effective compared to fine-tuning
    
    Challenges:
    - Retrieval quality affects final answer
    - Need good embedding model
    - Managing large document collections
    - Latency of retrieval + generation
    
    Improvements mentioned in production:
    - Hybrid search (keyword + semantic)
    - Reranking for better quality
    - Caching for common queries
    - Metadata filtering
    - Multi-stage retrieval
    """)
