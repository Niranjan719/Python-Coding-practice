"""
PYTHON FUNDAMENTALS FOR AI/ML INTERVIEWS
⭐ Easy to Medium difficulty questions

These questions test:
- List comprehensions & generators
- Dictionary operations & Counter
- String manipulation
- Lambda functions & map/filter
- Exception handling
- File I/O operations
"""

# ============================================================================
# Q1: STRING MANIPULATION - Tokenization Pattern
# ============================================================================
# Question: Implement a basic tokenizer that splits text into words and lowercases them
# (Foundation for NLP tasks)

def tokenize_text(text):
    """
    ⭐ Easy
    Tokenize text into lowercase words, removing punctuation
    
    Input: "Hello, World! How are you?"
    Output: ["hello", "world", "how", "are", "you"]
    
    Time: O(n), Space: O(n)
    """
    pass


# ============================================================================
# Q2: LIST COMPREHENSION - Filter and Transform
# ============================================================================
# Question: Extract and process data efficiently

def process_embeddings(embeddings, threshold=0.5):
    """
    ⭐ Easy
    Given a list of embeddings (floats), return indices where value > threshold
    
    Input: [0.1, 0.8, 0.3, 0.9, 0.2], threshold=0.5
    Output: [1, 3]
    """
    pass


# ============================================================================
# Q3: DICTIONARY OPERATIONS - Frequency Counter
# ============================================================================
# Question: Count word frequencies in text (Used in TF-IDF, word embeddings)

def word_frequency(text):
    """
    ⭐ Easy
    Return dictionary of word frequencies sorted by count (descending)
    
    Input: "the quick brown fox jumps over the lazy dog"
    Output: {'the': 2, 'quick': 1, 'brown': 1, ...}
    
    Tip: Use Counter from collections module
    """
    pass


# ============================================================================
# Q4: STRING MANIPULATION - Cleaning Data
# ============================================================================
# Question: Clean and normalize text for LLM input

def clean_text_for_llm(text):
    """
    ⭐ Easy
    Clean text by:
    - Converting to lowercase
    - Removing extra whitespace
    - Removing special characters (keep alphanumeric and spaces)
    
    Input: "  Hello!!! @#$  WORLD  "
    Output: "hello world"
    """
    pass


# ============================================================================
# Q5: LAMBDA & MAP/FILTER - Data Transformation
# ============================================================================
# Question: Batch process prompts efficiently

def batch_transform_prompts(prompts, operation="uppercase"):
    """
    ⭐⭐ Medium
    Apply transformation to batch of prompts using lambda
    Operations: 'uppercase', 'lowercase', 'add_prefix', 'remove_punctuation'
    
    Input: ["hello world", "python code"], operation="uppercase"
    Output: ["HELLO WORLD", "PYTHON CODE"]
    
    Tip: Use lambda with map() for efficient batch processing
    """
    pass


# ============================================================================
# Q6: GENERATOR FUNCTION - Memory Efficient Data Loading
# ============================================================================
# Question: Load large dataset efficiently for training

def batch_data_generator(data, batch_size=32):
    """
    ⭐⭐ Medium
    Create a generator that yields batches of data
    Used when loading large embeddings or documents
    
    Input: [1,2,3,4,5,6,7,8,9], batch_size=3
    Yields: [1,2,3], [4,5,6], [7,8,9]
    
    Benefit: Memory efficient for large datasets
    """
    pass


# ============================================================================
# Q7: EXCEPTION HANDLING - Robust API Calls
# ============================================================================
# Question: Handle errors in LLM API calls gracefully

def safe_api_call(api_func, *args, max_retries=3, **kwargs):
    """
    ⭐⭐ Medium
    Wrapper function that retries API call on failure
    
    Behavior:
    - Try to call api_func with given args
    - Retry up to max_retries times on exception
    - Log which attempt succeeded
    - Raise exception if all attempts fail
    
    Tip: Use try-except-finally pattern
    """
    pass


# ============================================================================
# Q8: DICTIONARY & NESTED DATA STRUCTURES - JSON Processing
# ============================================================================
# Question: Process API responses (common in LLM integrations)

def extract_llm_response(response_dict):
    """
    ⭐⭐ Medium
    Extract content from nested LLM API response safely
    
    Response format:
    {
        "choices": [
            {
                "message": {
                    "content": "The answer is...",
                    "role": "assistant"
                }
            }
        ]
    }
    
    Return: "The answer is..." or None if not found
    Tip: Use dict.get() for safe access
    """
    pass


# ============================================================================
# Q9: LIST SLICING & MANIPULATION - Prompt Chunking
# ============================================================================
# Question: Split long context into manageable chunks for RAG

def chunk_text(text, chunk_size=256, overlap=32):
    """
    ⭐⭐ Medium
    Split text into overlapping chunks
    Used in RAG to split documents into context windows
    
    Input: "abcdefghij", chunk_size=3, overlap=1
    Output: ["abc", "bcd", "cde", "def", "efg", "fgh", "ghij"]
    
    Tip: Use range() with step parameter
    """
    pass


# ============================================================================
# Q10: SORTING & SORTING KEY - Ranking Results
# ============================================================================
# Question: Sort search results by relevance score (RAG context)

def sort_documents_by_relevance(documents):
    """
    ⭐ Easy
    Sort documents list by relevance_score in descending order
    
    Input: [
        {'id': 1, 'text': 'doc1', 'relevance_score': 0.8},
        {'id': 2, 'text': 'doc2', 'relevance_score': 0.95},
        {'id': 3, 'text': 'doc3', 'relevance_score': 0.6}
    ]
    Output: [doc2, doc1, doc3]
    
    Tip: Use sorted() with key parameter
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE - Uncomment to see solutions
# ============================================================================

"""
SOLUTIONS:

# Q1: Tokenization
def tokenize_text(text):
    import string
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text.split()

# Q2: Embeddings Filter
def process_embeddings(embeddings, threshold=0.5):
    return [i for i, val in enumerate(embeddings) if val > threshold]

# Q3: Word Frequency
def word_frequency(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words).most_common())

# Q4: Text Cleaning
def clean_text_for_llm(text):
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = ' '.join(text.split())
    return text

# Q5: Batch Transform
def batch_transform_prompts(prompts, operation="uppercase"):
    ops = {
        'uppercase': lambda x: x.upper(),
        'lowercase': lambda x: x.lower(),
        'add_prefix': lambda x: f"Process: {x}",
        'remove_punctuation': lambda x: ''.join(c for c in x if c.isalnum() or c.isspace())
    }
    return list(map(ops[operation], prompts))

# Q6: Batch Generator
def batch_data_generator(data, batch_size=32):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

# Q7: Safe API Call
def safe_api_call(api_func, *args, max_retries=3, **kwargs):
    for attempt in range(max_retries):
        try:
            result = api_func(*args, **kwargs)
            print(f"Success on attempt {attempt + 1}")
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {str(e)}")
    
# Q8: Extract LLM Response
def extract_llm_response(response_dict):
    try:
        return response_dict.get('choices', [{}])[0].get('message', {}).get('content')
    except (KeyError, IndexError, TypeError):
        return None

# Q9: Text Chunking
def chunk_text(text, chunk_size=256, overlap=32):
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(text), step):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Q10: Sort Documents
def sort_documents_by_relevance(documents):
    return sorted(documents, key=lambda d: d['relevance_score'], reverse=True)
"""


# ============================================================================
# PRACTICE SECTION
# ============================================================================

if __name__ == "__main__":
    # Q1: Test Tokenization
    print("Q1: Tokenization")
    result = tokenize_text("Hello, World! How are you?")
    print(f"Result: {result}")
    print(f"Expected: ['hello', 'world', 'how', 'are', 'you']")
    print()
    
    # Q2: Test Embeddings Filter
    print("Q2: Embeddings Filter")
    result = process_embeddings([0.1, 0.8, 0.3, 0.9, 0.2], threshold=0.5)
    print(f"Result: {result}")
    print(f"Expected: [1, 3]")
    print()
    
    # Q3: Test Word Frequency
    print("Q3: Word Frequency")
    result = word_frequency("the quick brown fox jumps over the lazy dog")
    print(f"Result: {result}")
    print()
    
    # Q4: Test Text Cleaning
    print("Q4: Clean Text")
    result = clean_text_for_llm("  Hello!!! @#$  WORLD  ")
    print(f"Result: '{result}'")
    print(f"Expected: 'hello world'")
    print()
    
    # Q9: Test Text Chunking
    print("Q9: Text Chunking")
    result = chunk_text("abcdefghij", chunk_size=3, overlap=1)
    print(f"Result: {result}")
    print(f"Expected: ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghij']")
