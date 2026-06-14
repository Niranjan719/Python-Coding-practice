"""
API INTEGRATION & REST DESIGN FOR AI/ML INTERVIEWS
⭐⭐ Medium to Hard difficulty questions

These questions test:
- REST API design principles
- Error handling and retries
- Rate limiting and throttling
- Async operations
- API response handling
- Integration patterns
"""

# ============================================================================
# Q1: BASIC REST CLIENT - API Call Wrapper
# ============================================================================
# Question: Create a simple REST API client

class SimpleAPIClient:
    """
    ⭐⭐ Medium
    Basic REST client for calling external APIs
    
    Features:
    - GET, POST methods
    - Headers management
    - Response parsing
    - Error handling
    
    Example:
    client = SimpleAPIClient(base_url="https://api.openai.com")
    response = client.get("/models")
    """
    
    def __init__(self, base_url, api_key=None, timeout=10):
        """Initialize API client with base URL and API key"""
        pass
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        pass
    
    def post(self, endpoint, data=None, json=None):
        """Make POST request"""
        pass


# ============================================================================
# Q2: RETRY LOGIC WITH EXPONENTIAL BACKOFF
# ============================================================================
# Question: Handle transient API failures

def api_call_with_retry(func, max_retries=3, backoff_factor=2):
    """
    ⭐⭐ Medium
    Call API with exponential backoff on failure
    
    Strategy:
    - Retry 1: Wait 1 second
    - Retry 2: Wait 2 seconds
    - Retry 3: Wait 4 seconds
    
    Input:
    func = lambda: llm_api.generate("prompt")
    max_retries = 3
    backoff_factor = 2
    
    Behavior:
    - Try calling func()
    - On failure, wait and retry
    - Only retry on transient errors (429, 503, timeout)
    - Raise exception if all retries fail
    
    Used for: LLM API calls, rate limiting handling
    
    Time: O(1) per call, but takes longer with retries
    """
    pass


# ============================================================================
# Q3: RATE LIMITING - Token Bucket Algorithm
# ============================================================================
# Question: Implement client-side rate limiting

class RateLimiter:
    """
    ⭐⭐ Medium
    Token bucket rate limiter for API calls
    
    Concept:
    - Start with N tokens in bucket
    - Each call costs 1 token
    - Tokens refill at rate R per second
    - Wait if no tokens available
    
    Example:
    limiter = RateLimiter(capacity=5, refill_rate=1)
    
    for i in range(10):
        limiter.acquire()  # Wait if needed
        api_call()
    
    Used by: AWS SDK, many API clients
    Prevents: Rate limit violations, HTTP 429 errors
    """
    
    def __init__(self, capacity=5, refill_rate=1):
        """capacity: max tokens, refill_rate: tokens/sec"""
        pass
    
    def acquire(self, tokens=1):
        """Wait until tokens available, then consume"""
        pass
    
    def available_tokens(self):
        """Return current token count"""
        pass


# ============================================================================
# Q4: BATCH API CALLS - Efficient Processing
# ============================================================================
# Question: Process multiple items with API

def batch_api_call(items, api_func, batch_size=10):
    """
    ⭐⭐ Medium
    Process items in batches through API
    
    Benefit: Some APIs charge per call, batching reduces cost
    
    Example:
    items = ["text1", "text2", ..., "text1000"]
    
    def embed_batch(texts):
        return embedding_api.embed(texts)
    
    results = batch_api_call(items, embed_batch, batch_size=100)
    
    Instead of:
    - 1000 calls @ $0.01 = $10
    Do:
    - 10 batch calls @ $0.09 = $0.90
    
    Input:
    - items: list of items to process
    - api_func: function that takes list and returns results
    - batch_size: items per batch
    
    Output: Combined results from all batches
    
    Time: O(n/batch_size) API calls
    """
    pass


# ============================================================================
# Q5: ASYNC API CALLS - Concurrent Requests
# ============================================================================
# Question: Speed up multiple API calls

async def async_api_calls(queries, api_func, max_concurrent=5):
    """
    ⭐⭐ Medium
    Make multiple API calls concurrently
    
    Benefits:
    - Sequential: 5 calls × 1 sec = 5 seconds
    - Concurrent: 5 calls = 1 second (if max_concurrent=5)
    
    Input:
    queries = ["What is AI?", "What is ML?", "What is RAG?"]
    api_func = llm.generate  # Async function
    max_concurrent = 3
    
    Output: Results in same order as input
    [response1, response2, response3]
    
    Tip: Use asyncio.Semaphore for concurrency limit
    """
    pass


# ============================================================================
# Q6: API RESPONSE PARSING - Handling Different Formats
# ============================================================================
# Question: Parse various API response formats

def parse_api_response(response, response_type="json"):
    """
    ⭐ Easy
    Parse API response based on format
    
    Supported formats: json, xml, text, csv
    
    Input:
    response = {
        'status_code': 200,
        'content': '{"result": "success", "data": [...]}'
    }
    response_type = "json"
    
    Output: Parsed data or None if error
    
    Error handling:
    - Invalid JSON -> log warning, return None
    - Non-200 status -> raise exception
    - Missing required fields -> return None
    """
    pass


# ============================================================================
# Q7: API KEY MANAGEMENT - Secure Credential Handling
# ============================================================================
# Question: Safely manage API credentials

class SecureAPIKeyManager:
    """
    ⭐⭐ Medium
    Manage API keys securely
    
    Best practices:
    - Never commit keys to git
    - Load from environment variables
    - Support rotating keys
    - Log API usage without exposing keys
    
    Example:
    manager = SecureAPIKeyManager()
    key = manager.get_key("openai")  # From env var OPENAI_API_KEY
    
    Log: "Called OpenAI API with key ***xyz" (mask key)
    """
    
    def __init__(self):
        """Initialize and load keys from environment"""
        pass
    
    def get_key(self, service_name):
        """Get API key for service"""
        pass
    
    def set_key(self, service_name, key):
        """Set/update API key (runtime)"""
        pass


# ============================================================================
# Q8: CIRCUIT BREAKER PATTERN - Graceful Degradation
# ============================================================================
# Question: Prevent cascading failures

class CircuitBreaker:
    """
    ⭐⭐ Medium
    Prevent repeated calls to failing service
    
    States:
    1. CLOSED: Normal operation, calls go through
    2. OPEN: Service failing, calls rejected immediately
    3. HALF_OPEN: Testing if service recovered
    
    Behavior:
    - Track consecutive failures
    - After N failures -> OPEN (fail fast)
    - After T seconds in OPEN -> HALF_OPEN (test recovery)
    - If test succeeds -> CLOSED
    
    Example:
    breaker = CircuitBreaker(failure_threshold=5, timeout=60)
    
    try:
        result = breaker.call(api_function)
    except CircuitBreakerOpen:
        # Use fallback or cached response
        result = get_cached_response()
    """
    
    def __init__(self, failure_threshold=5, timeout=60):
        """failure_threshold: failures before opening"""
        pass
    
    def call(self, func, *args, **kwargs):
        """Call function through circuit breaker"""
        pass


# ============================================================================
# Q9: REQUEST/RESPONSE LOGGING - Debugging and Audit
# ============================================================================
# Question: Log API interactions for debugging

def log_api_call(method, url, request_data, response_data, status_code, duration):
    """
    ⭐ Easy
    Log API call for debugging and audit
    
    What to log:
    - Timestamp
    - Method (GET, POST)
    - URL/Endpoint
    - Request size (not content for privacy)
    - Response status
    - Duration
    - Error messages
    
    What NOT to log:
    - API keys
    - Authentication tokens
    - Sensitive user data
    - Full response body (if large)
    
    Input:
    - method: "POST"
    - url: "https://api.openai.com/v1/chat/completions"
    - request_data: {"model": "gpt-4", "messages": [...]}
    - response_data: {"id": "chatcmpl-...", "choices": [...]}
    - status_code: 200
    - duration: 2.34 (seconds)
    
    Output: Formatted log entry
    """
    pass


# ============================================================================
# Q10: WEBHOOK HANDLER - Event-Driven API
# ============================================================================
# Question: Handle incoming webhook events

class WebhookHandler:
    """
    ⭐⭐ Medium
    Handle incoming webhooks from services
    
    Example webhook events:
    - LLM generation completed
    - Document processing finished
    - Training job failed
    
    Requirements:
    - Verify webhook signature (security)
    - Route to correct handler
    - Handle retries from sender
    - Return 200 quickly (don't process in request)
    
    Best practice:
    1. Receive webhook
    2. Verify signature
    3. Queue for async processing
    4. Return 200
    5. Process in background
    
    Example:
    handler = WebhookHandler()
    handler.register("llm.complete", on_llm_complete)
    handler.register("training.failed", on_training_failed)
    
    handler.process(webhook_data)  # Routes and processes
    """
    
    def __init__(self, secret_key=None):
        """secret_key: for webhook signature verification"""
        pass
    
    def register(self, event_type, handler_func):
        """Register handler for event type"""
        pass
    
    def process(self, event_data):
        """Receive and process webhook event"""
        pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q2: Retry with Backoff
import time
import random

def api_call_with_retry(func, max_retries=3, backoff_factor=2):
    wait_time = 1
    
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time + random.uniform(0, 1))  # Add jitter
            wait_time *= backoff_factor

# Q3: Rate Limiter
import time
import threading

class RateLimiter:
    def __init__(self, capacity=5, refill_rate=1):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = threading.Lock()
    
    def acquire(self, tokens=1):
        while self.available_tokens() < tokens:
            time.sleep(0.1)
        
        with self.lock:
            self.tokens -= tokens
    
    def available_tokens(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        return self.tokens

# Q4: Batch API Call
def batch_api_call(items, api_func, batch_size=10):
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        batch_results = api_func(batch)
        results.extend(batch_results)
    return results

# Q9: Log API Call
import logging
from datetime import datetime

def log_api_call(method, url, request_data, response_data, status_code, duration):
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'method': method,
        'url': url,
        'request_size': len(str(request_data)),
        'response_size': len(str(response_data)),
        'status_code': status_code,
        'duration': duration
    }
    
    logging.info(f"API Call: {log_entry}")
    return log_entry
"""


if __name__ == "__main__":
    print("API Integration Questions")
    print("=" * 50)
