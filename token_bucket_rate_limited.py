# Create a token bukcet rate limited in simple and easy way
import time
import threading
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill_time
        new_tokens = int(elapsed * self.refill_rate)
        if new_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_refill_time = now

    def consume(self, tokens=1):
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
        
# Example usage
if __name__ == "__main__":
    bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 tokens max, 1 token per second

    for i in range(10):
        if bucket.consume():
            print(f"Request {i} allowed")
        else:
            print(f"Request {i} denied")
        time.sleep(0.5)  # Simulate time between requests