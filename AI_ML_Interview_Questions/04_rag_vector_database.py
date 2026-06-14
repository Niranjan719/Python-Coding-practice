"""
RAG (RETRIEVAL AUGMENTED GENERATION) & VECTOR DATABASE QUESTIONS
⭐⭐ Medium to Hard difficulty questions

These questions test:
- Document chunking and splitting strategies
- Vector similarity search
- Ranking and reranking
- Cache management for LLM context
- Retrieval pipeline design
- Context aggregation for prompt engineering
"""

# ============================================================================
# Q1: DOCUMENT CHUNKING - Splitting Long Documents
# ============================================================================
# Question: Split documents for RAG retrieval

def chunk_documents_overlap(documents, chunk_size=256, overlap=32):
    """
    ⭐⭐ Medium
    Split documents into overlapping chunks for RAG
    Overlap helps maintain context across chunks
    
    Input:
    documents = [
        "Document 1: This is a very long document that needs to be split...",
        "Document 2: Another long document..."
    ]
    chunk_size = 256
    overlap = 32
    
    Output:
    [
        {'doc_id': 0, 'chunk_id': 0, 'text': '...', 'position': 0},
        {'doc_id': 0, 'chunk_id': 1, 'text': '...', 'position': 224},
        ...
    ]
    
    Important for: Maintaining context across documents
    """
    pass


# ============================================================================
# Q2: VECTOR DATABASE QUERY - Similarity Search
# ============================================================================
# Question: Find k-nearest neighbors in embedding space

def find_similar_documents(query_embedding, document_embeddings, k=5, threshold=0.5):
    """
    ⭐⭐ Medium
    Find top-k most similar documents to query
    Simulates vector DB search (like Pinecone, Weaviate, FAISS)
    
    Input:
    query_embedding = [0.1, 0.2, 0.3, ...]  # 768-dim (from embedding model)
    document_embeddings = [
        {'id': 'doc1', 'embedding': [0.11, 0.19, 0.29, ...]},
        {'id': 'doc2', 'embedding': [0.9, 0.8, 0.7, ...]},
        ...
    ]
    k = 5
    threshold = 0.5 (minimum similarity)
    
    Output: [
        {'id': 'doc1', 'similarity': 0.98},
        {'id': 'doc3', 'similarity': 0.87},
        ...
    ]
    
    Tip: Use cosine_similarity from Q4 in nlp_llm file
    """
    pass


# ============================================================================
# Q3: RERANKING - Improving Retrieval Quality
# ============================================================================
# Question: Rerank retrieved documents by relevance

def rerank_documents(query, documents, ranker_model_scores=None):
    """
    ⭐⭐ Medium
    Rerank documents using relevance model
    Often a second pass to improve precision
    
    Two-stage retrieval:
    1. Fast retrieval: Use vector similarity (k=20)
    2. Reranking: Use slower but better model (top k=5)
    
    Input:
    query = "How does RAG work?"
    documents = [
        {'id': 'doc1', 'text': 'RAG combines retrieval...', 'bm25_score': 0.8},
        {'id': 'doc2', 'text': 'Vector databases store...', 'bm25_score': 0.6},
    ]
    ranker_model_scores = {'doc1': 0.95, 'doc2': 0.4}  # From cross-encoder
    
    Output: Sorted by reranker scores
    [
        {'id': 'doc1', 'score': 0.95},
        {'id': 'doc2', 'score': 0.4}
    ]
    """
    pass


# ============================================================================
# Q4: CONTEXT WINDOW MANAGEMENT - Token Budget
# ============================================================================
# Question: Fit documents into LLM context window

def fit_documents_to_context(documents, max_tokens=2048, reserve_for_response=512):
    """
    ⭐⭐ Medium
    Select documents that fit in LLM context window
    
    LLM context budgeting:
    - GPT-4: 8k, 32k, or 128k tokens
    - Claude: 100k tokens
    - Llama: 4k, 8k, or 32k tokens
    
    Input:
    documents = [
        {'id': 'doc1', 'text': '...', 'token_count': 300},
        {'id': 'doc2', 'text': '...', 'token_count': 500},
        {'id': 'doc3', 'text': '...', 'token_count': 1200},
    ]
    max_tokens = 2048
    reserve_for_response = 512
    available = 2048 - 512 = 1536 tokens
    
    Output: ['doc1', 'doc2'] (300+500 = 800 tokens)
    
    Note: Don't include doc3 (would exceed limit)
    """
    pass


# ============================================================================
# Q5: METADATA FILTERING - Filtered Search
# ============================================================================
# Question: Search with metadata constraints

def search_with_metadata_filter(query_embedding, documents, filters):
    """
    ⭐⭐ Medium
    Perform similarity search with metadata filters
    Like: search for "AI safety" but only in docs from 2024
    
    Input:
    query_embedding = [0.1, 0.2, ...]
    documents = [
        {'embedding': [...], 'date': 2024, 'category': 'AI', 'score': 0.9},
        {'embedding': [...], 'date': 2023, 'category': 'ML', 'score': 0.7},
        {'embedding': [...], 'date': 2024, 'category': 'Safety', 'score': 0.8},
    ]
    filters = {'date': 2024, 'category': 'AI'}
    
    Output: Only docs matching filters, ranked by similarity
    [
        {'embedding': [...], 'date': 2024, 'category': 'AI', 'score': 0.9}
    ]
    """
    pass


# ============================================================================
# Q6: HYBRID SEARCH - Combining BM25 and Vector Search
# ============================================================================
# Question: Combine keyword and semantic search

def hybrid_search(query, documents, bm25_results, vector_results, alpha=0.5):
    """
    ⭐⭐ Medium
    Combine BM25 (keyword) and vector search results
    Often better than either alone
    
    BM25: Good for exact keywords, fast
    Vector: Good for semantic meaning
    
    Input:
    bm25_results = {
        'doc1': 0.9,  # BM25 score
        'doc2': 0.7,
    }
    vector_results = {
        'doc1': 0.8,  # Cosine similarity
        'doc3': 0.95,
    }
    alpha = 0.5  # Weight for BM25 vs Vector
    
    Combined Score = alpha * bm25_score + (1-alpha) * vector_score
    
    Output: Ranked by combined score
    [
        {'id': 'doc1', 'score': 0.85},  # 0.5*0.9 + 0.5*0.8
        {'id': 'doc3', 'score': 0.475}, # 0.5*0 + 0.5*0.95
        {'id': 'doc2', 'score': 0.35},  # 0.5*0.7 + 0.5*0
    ]
    """
    pass


# ============================================================================
# Q7: CACHE FOR RAG - Prompt Caching
# ============================================================================
# Question: Cache retrieved context to reduce API costs

class RAGCache:
    """
    ⭐⭐ Medium
    Cache RAG results to avoid re-retrieving same query
    
    Benefit: Reduce vector DB and LLM API calls
    
    Methods needed:
    - get(query) -> cached_context or None
    - set(query, context, ttl=3600)
    - clear()
    
    Example usage:
    cache = RAGCache()
    
    # First time: hits vector DB
    context = cache.get("What is RAG?")  # None
    context = retrieve_from_db("What is RAG?")
    cache.set("What is RAG?", context)
    
    # Second time: hits cache
    context = cache.get("What is RAG?")  # Returns cached context
    """
    def __init__(self, max_size=100):
        pass
    
    def get(self, query):
        """Retrieve cached context for query"""
        pass
    
    def set(self, query, context, ttl=3600):
        """Cache context with optional TTL"""
        pass
    
    def clear(self):
        """Clear cache"""
        pass


# ============================================================================
# Q8: RETRIEVAL METRICS - Evaluating RAG Quality
# ============================================================================
# Question: Evaluate if retrieved docs are relevant

def calculate_rag_metrics(ground_truth_docs, retrieved_docs, top_k=5):
    """
    ⭐⭐ Medium
    Calculate Precision, Recall, F1 for retrieval
    
    Precision: Of top-k retrieved, how many are correct?
    Recall: Of all correct docs, how many did we retrieve?
    F1: Harmonic mean of precision and recall
    
    Input:
    ground_truth_docs = {'doc1', 'doc3', 'doc5'}  # Correct docs
    retrieved_docs = ['doc1', 'doc2', 'doc3']  # What we retrieved
    top_k = 5
    
    Output:
    {
        'precision': 0.67,  # 2 correct out of 3 retrieved
        'recall': 0.67,     # 2 correct out of 3 ground truth
        'f1': 0.67
    }
    
    Precision = TP / (TP + FP)
    Recall = TP / (TP + FN)
    """
    pass


# ============================================================================
# Q9: QUERY EXPANSION - Improving Retrieval Coverage
# ============================================================================
# Question: Improve search by expanding query

def expand_query(query, llm_generated_variations=None):
    """
    ⭐⭐ Medium
    Expand query with synonyms and variations
    Improves recall by searching multiple ways
    
    Input:
    query = "How does transformer architecture work?"
    
    Variations could be:
    - "What is transformer model?"
    - "Explain attention mechanism in transformers"
    - "How do transformer networks function?"
    
    Output: [original_query] + [variation1, variation2, ...]
    
    Then search for each variation and combine results
    """
    pass


# ============================================================================
# Q10: CONTEXT FORMATTING - Building LLM Prompt
# ============================================================================
# Question: Format retrieved context for prompt

def format_rag_prompt(query, retrieved_documents, system_prompt=""):
    """
    ⭐ Easy
    Format retrieval result into prompt for LLM
    
    Input:
    query = "How does RAG work?"
    retrieved_documents = [
        {'id': 'doc1', 'text': 'RAG combines...', 'score': 0.95},
        {'id': 'doc2', 'text': 'Vector stores...', 'score': 0.87},
    ]
    system_prompt = "You are an AI expert."
    
    Output: Formatted prompt string
    
    Typical format:
    ```
    You are an AI expert.
    
    Use the following context to answer the question:
    
    Context:
    [1] RAG combines... (from doc1, score: 0.95)
    [2] Vector stores... (from doc2, score: 0.87)
    
    Question: How does RAG work?
    
    Answer:
    ```
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q1: Document Chunking
def chunk_documents_overlap(documents, chunk_size=256, overlap=32):
    chunks = []
    for doc_id, doc in enumerate(documents):
        words = doc.split()
        step = chunk_size - overlap
        
        for i in range(0, len(words), step):
            chunk_words = words[i:i+chunk_size]
            chunks.append({
                'doc_id': doc_id,
                'chunk_id': len([c for c in chunks if c['doc_id'] == doc_id]),
                'text': ' '.join(chunk_words),
                'position': i
            })
    
    return chunks

# Q2: Similar Documents
def find_similar_documents(query_embedding, document_embeddings, k=5, threshold=0.5):
    from math import sqrt
    
    similarities = []
    
    for doc in document_embeddings:
        dot_product = sum(q * e for q, e in zip(query_embedding, doc['embedding']))
        mag_q = sqrt(sum(q**2 for q in query_embedding))
        mag_e = sqrt(sum(e**2 for e in doc['embedding']))
        
        similarity = dot_product / (mag_q * mag_e) if mag_q and mag_e else 0
        
        if similarity >= threshold:
            similarities.append({
                'id': doc['id'],
                'similarity': similarity
            })
    
    return sorted(similarities, key=lambda x: x['similarity'], reverse=True)[:k]

# Q3: Reranking
def rerank_documents(query, documents, ranker_model_scores=None):
    if ranker_model_scores:
        for doc in documents:
            doc['final_score'] = ranker_model_scores.get(doc['id'], 0)
    else:
        for doc in documents:
            doc['final_score'] = doc.get('bm25_score', 0)
    
    return sorted(documents, key=lambda x: x['final_score'], reverse=True)

# Q4: Context Window Fit
def fit_documents_to_context(documents, max_tokens=2048, reserve_for_response=512):
    available_tokens = max_tokens - reserve_for_response
    selected = []
    total_tokens = 0
    
    for doc in sorted(documents, key=lambda x: x['token_count']):
        if total_tokens + doc['token_count'] <= available_tokens:
            selected.append(doc['id'])
            total_tokens += doc['token_count']
    
    return selected

# Q6: Hybrid Search
def hybrid_search(query, documents, bm25_results, vector_results, alpha=0.5):
    combined_scores = {}
    
    for doc_id in set(list(bm25_results.keys()) + list(vector_results.keys())):
        bm25_score = bm25_results.get(doc_id, 0)
        vector_score = vector_results.get(doc_id, 0)
        combined_scores[doc_id] = alpha * bm25_score + (1 - alpha) * vector_score
    
    return sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)

# Q8: RAG Metrics
def calculate_rag_metrics(ground_truth_docs, retrieved_docs, top_k=5):
    retrieved_set = set(retrieved_docs[:top_k])
    ground_set = set(ground_truth_docs)
    
    tp = len(retrieved_set & ground_set)
    fp = len(retrieved_set - ground_set)
    fn = len(ground_set - retrieved_set)
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {'precision': precision, 'recall': recall, 'f1': f1}

# Q10: Format RAG Prompt
def format_rag_prompt(query, retrieved_documents, system_prompt=""):
    context_str = "\\n".join([
        f"[{i+1}] {doc['text']} (relevance: {doc.get('score', 0):.2f})"
        for i, doc in enumerate(retrieved_documents)
    ])
    
    prompt = f\"\"\"{system_prompt}

Use the following context to answer the question:

Context:
{context_str}

Question: {query}

Answer:\"\"\"
    
    return prompt
"""


if __name__ == "__main__":
    print("RAG & Vector Database Questions")
    print("=" * 50)
    print()
