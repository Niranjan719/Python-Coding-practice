# Token bucket rate limiter without classes - simple function-based approach
import time
import threading

# Global dictionary to store bucket state
bucket = {
    'tokens': 5,
    'capacity': 5,
    'refill_rate': 1,
    'last_refill_time': time.time()
}

lock = threading.Lock()

def refill():
    """Add tokens back to the bucket based on time elapsed"""
    now = time.time()
    elapsed = now - bucket['last_refill_time']
    new_tokens = int(elapsed * bucket['refill_rate'])
    
    if new_tokens > 0:
        bucket['tokens'] = min(bucket['capacity'], bucket['tokens'] + new_tokens)
        bucket['last_refill_time'] = now

def consume(tokens=1):
    """Try to consume tokens. Returns True if allowed, False if denied"""
    with lock:
        refill()  # Refill first
        
        if bucket['tokens'] >= tokens:
            bucket['tokens'] -= tokens
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Initialize bucket
    bucket['capacity'] = 5
    bucket['refill_rate'] = 1
    bucket['tokens'] = 5
    bucket['last_refill_time'] = time.time()
    
    for i in range(10):
        if consume():
            print(f"Request {i} allowed")
        else:
            print(f"Request {i} denied")
        time.sleep(0.5)  # Simulate time between requests
