"""
NLP & LLM FUNDAMENTALS FOR AI/ML INTERVIEWS
⭐⭐ Medium to Hard difficulty questions

These questions test:
- Text preprocessing for LLMs
- Tokenization and encoding
- Embedding concepts
- TF-IDF and text similarity
- Named Entity Recognition basics
- Sentiment analysis concepts
"""

# ============================================================================
# Q1: TOKENIZATION & ATTENTION MASK
# ============================================================================
# Question: Prepare tokens for LLM input

def create_attention_mask(tokens, max_length=512):
    """
    ⭐⭐ Medium
    Create attention mask for transformer models
    1 for real tokens, 0 for padding
    
    Input: tokens=['hello', 'world'], max_length=5
    Output: [1, 1, 0, 0, 0]
    
    Used in: BERT, GPT, all transformer models
    """
    pass


# ============================================================================
# Q2: TOKENIZATION WITH SUBWORD TOKENS
# ============================================================================
# Question: Implement BPE-like tokenization

def byte_pair_encoding_simple(text, num_merges=10):
    """
    ⭐⭐⭐ Hard
    Simplified Byte Pair Encoding (used by GPT, Mistral)
    
    Process:
    1. Start with character-level tokens
    2. Find most common adjacent pair
    3. Merge and repeat
    
    Input: "hello", num_merges=2
    Output: Tokenized representation
    
    Note: Real BPE is more complex (used by tiktoken)
    """
    pass


# ============================================================================
# Q3: TF-IDF CALCULATION - Document Relevance
# ============================================================================
# Question: Calculate TF-IDF for RAG document ranking

def calculate_tfidf(documents, query):
    """
    ⭐⭐ Medium
    Calculate TF-IDF scores for query against documents
    Used to rank relevance of documents in RAG
    
    TF-IDF = (Term Frequency) × (Inverse Document Frequency)
    TF = (count of term in doc) / (total terms in doc)
    IDF = log(total docs / docs containing term)
    
    Input:
    documents = ["ai is great", "machine learning is powerful", "ai and ml"]
    query = "ai"
    
    Output: [score1, score2, score3] - relevance scores
    
    Time: O(n*m), Space: O(n*m)
    """
    pass


# ============================================================================
# Q4: COSINE SIMILARITY - Embedding Comparison
# ============================================================================
# Question: Compare two embeddings

def cosine_similarity(vec1, vec2):
    """
    ⭐⭐ Medium
    Calculate cosine similarity between two vectors
    Used in embedding-based RAG to find similar documents
    
    Formula: cos(A,B) = (A·B) / (|A| × |B|)
    Range: -1 to 1 (higher = more similar)
    
    Input: 
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    
    Output: similarity score between 0 and 1
    
    Time: O(n), Space: O(1)
    """
    pass


# ============================================================================
# Q5: N-GRAM EXTRACTION - Language Patterns
# ============================================================================
# Question: Extract n-grams for analysis

def extract_ngrams(text, n=2):
    """
    ⭐⭐ Medium
    Extract n-grams (sequences of n words) from text
    Used for language modeling, pattern detection
    
    Input: "the quick brown fox jumps", n=2
    Output: [('the', 'quick'), ('quick', 'brown'), ('brown', 'fox'), ('fox', 'jumps')]
    
    Common uses:
    - Language modeling
    - Finding repeated phrases
    - Plagiarism detection
    
    Time: O(n), Space: O(n)
    """
    pass


# ============================================================================
# Q6: STOP WORDS REMOVAL - Text Cleaning
# ============================================================================
# Question: Clean text for embedding

def remove_stopwords(text, stopwords=None):
    """
    ⭐ Easy
    Remove common words that don't add meaning
    
    Common stopwords: "the", "a", "is", "are", "and", etc.
    
    Input: "the quick brown fox is jumping over the lazy dog"
    Output: "quick brown fox jumping lazy dog"
    
    Note: Stop words vary by domain
    - General NLP: nltk stopwords
    - Technical docs: different set
    - Medical: different set
    
    Time: O(n), Space: O(1)
    """
    pass


# ============================================================================
# Q7: WORD EMBEDDING BASICS - Vector Representation
# ============================================================================
# Question: Create simple word embeddings

def create_word_embedding_matrix(vocabulary, embedding_dim=300):
    """
    ⭐⭐ Medium
    Create random initial embedding matrix for vocabulary
    Like Word2Vec, GloVe initialization
    
    Input:
    vocabulary = ['hello', 'world', 'ai', 'machine']
    embedding_dim = 300
    
    Output:
    dict {
        'hello': [0.1, 0.2, ..., 0.3],  # 300-dim vector
        'world': [0.5, 0.1, ..., 0.2],
        ...
    }
    
    Tip: Use random initialization with numpy
    """
    pass


# ============================================================================
# Q8: ATTENTION SCORES - Core LLM Concept
# ============================================================================
# Question: Calculate attention weights

def calculate_attention_scores(query, key_matrix):
    """
    ⭐⭐ Medium
    Calculate scaled dot-product attention scores
    Core mechanism in Transformers (GPT, BERT, etc.)
    
    Formula: Attention = softmax(Q·K^T / sqrt(d_k))
    
    Input:
    query = [0.1, 0.2, 0.3]  # 1 query vector
    key_matrix = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]  # 3 key vectors
    
    Output: Attention weights [0.3, 0.4, 0.3] (sum=1)
    
    Meaning: How much to attend to each position
    """
    pass


# ============================================================================
# Q9: NAMED ENTITY RECOGNITION (NER) - Entity Extraction
# ============================================================================
# Question: Extract entities from text (simplified)

def simple_entity_extraction(text, entity_keywords):
    """
    ⭐⭐ Medium
    Extract entities based on keyword matching
    Simplified version of NER (real NER uses ML models)
    
    Input:
    text = "Apple CEO Tim Cook announced new products in San Francisco"
    entity_keywords = {
        'COMPANY': ['Apple', 'Google', 'Microsoft'],
        'PERSON': ['Tim Cook', 'Steve Jobs'],
        'LOCATION': ['San Francisco', 'New York']
    }
    
    Output:
    [
        ('Apple', 'COMPANY', 0),
        ('Tim Cook', 'PERSON', 10),
        ('San Francisco', 'LOCATION', 50)
    ]
    
    Returns: (entity, type, position)
    """
    pass


# ============================================================================
# Q10: SENTIMENT ANALYSIS - Text Classification Concept
# ============================================================================
# Question: Simple sentiment scoring

def simple_sentiment_score(text, positive_words, negative_words):
    """
    ⭐ Easy
    Calculate sentiment score based on word lists
    Simplified version of sentiment analysis
    
    Input:
    text = "This product is amazing and excellent but expensive"
    positive_words = {'amazing', 'excellent', 'great', 'good'}
    negative_words = {'bad', 'terrible', 'expensive', 'poor'}
    
    Output: score (1.0 = very positive, -1.0 = very negative, 0.0 = neutral)
    Formula: (positive_count - negative_count) / total_count
    
    Time: O(n), Space: O(1)
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q1: Attention Mask
def create_attention_mask(tokens, max_length=512):
    mask = [1] * len(tokens) + [0] * (max_length - len(tokens))
    return mask[:max_length]

# Q3: TF-IDF
def calculate_tfidf(documents, query):
    import math
    from collections import Counter
    
    query_words = query.lower().split()
    scores = []
    
    for doc in documents:
        doc_words = doc.lower().split()
        tf_sum = 0
        
        for word in query_words:
            # TF: count in doc / total words in doc
            tf = doc_words.count(word) / len(doc_words)
            
            # IDF: log(total docs / docs with word)
            doc_count = sum(1 for d in documents if word in d.lower())
            idf = math.log(len(documents) / (doc_count + 1))
            
            tf_sum += tf * idf
        
        scores.append(tf_sum)
    
    return scores

# Q4: Cosine Similarity
def cosine_similarity(vec1, vec2):
    import math
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a**2 for a in vec1))
    mag2 = math.sqrt(sum(b**2 for b in vec2))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    
    return dot_product / (mag1 * mag2)

# Q5: N-grams
def extract_ngrams(text, n=2):
    words = text.lower().split()
    return list(zip(*[words[i:] for i in range(n)]))

# Q6: Stop Words
def remove_stopwords(text, stopwords=None):
    if stopwords is None:
        stopwords = {'the', 'a', 'is', 'are', 'and', 'or', 'in', 'on', 'at', 'to', 'for'}
    
    words = text.lower().split()
    return ' '.join([w for w in words if w not in stopwords])

# Q7: Word Embeddings
def create_word_embedding_matrix(vocabulary, embedding_dim=300):
    import random
    return {word: [random.uniform(-0.5, 0.5) for _ in range(embedding_dim)] 
            for word in vocabulary}

# Q8: Attention Scores
def calculate_attention_scores(query, key_matrix):
    import math
    
    # Scaled dot-product
    scores = []
    scaling_factor = math.sqrt(len(query))
    
    for key in key_matrix:
        dot_product = sum(q * k for q, k in zip(query, key)) / scaling_factor
        scores.append(dot_product)
    
    # Softmax
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    
    return [e / sum_exp for e in exp_scores]

# Q9: Entity Extraction
def simple_entity_extraction(text, entity_keywords):
    entities = []
    for entity_type, keywords in entity_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                pos = text.lower().find(keyword.lower())
                entities.append((keyword, entity_type, pos))
    
    return sorted(entities, key=lambda x: x[2])

# Q10: Sentiment Score
def simple_sentiment_score(text, positive_words, negative_words):
    words = text.lower().split()
    
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    
    if len(words) == 0:
        return 0.0
    
    return (pos_count - neg_count) / len(words)
"""


if __name__ == "__main__":
    # Q1: Test Attention Mask
    print("Q1: Attention Mask")
    result = create_attention_mask(['hello', 'world'], max_length=5)
    print(f"Result: {result}")
    print(f"Expected: [1, 1, 0, 0, 0]")
    print()
    
    # Q5: Test N-grams
    print("Q5: N-grams")
    result = extract_ngrams("the quick brown fox", n=2)
    print(f"Result: {result}")
    print()
    
    # Q4: Test Cosine Similarity
    print("Q4: Cosine Similarity")
    result = cosine_similarity([1, 2, 3], [4, 5, 6])
    print(f"Result: {result:.4f}")
    print()
