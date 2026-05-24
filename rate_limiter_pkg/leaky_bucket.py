from time import time, sleep
from collections import deque
from rate_limiter_pkg.rate_limiter import RateLimiter


class LeakyBucket(RateLimiter):

    def __init__(self, capacity: int, leak_rate: int) -> None:

        self.capacity = capacity
        self.leak_rate = leak_rate
        self.bucket = deque()
        self.last_leak = time()

    def is_req_allowed(self) -> bool:

        now = time()

        # If the elapsed time is large enough, the leaked request count may exceed
        # the number of requests in the bucket. In that case, empty the bucket.
        leaked_req_count = min(int((now - self.last_leak) * self.leak_rate), len(self.bucket))

        # remove leaked requests
        for _ in range(leaked_req_count):
            self.bucket.popleft()

        # preserve precise timing
        if leaked_req_count > 0:
            self.last_leak = now

        # reject if full
        if len(self.bucket) >= self.capacity:
            return False

        # accept request
        self.bucket.append(now)

        return True


if __name__ == "__main__":
    lb = LeakyBucket(capacity=4, leak_rate=2)
    for i in range(1, 19):
        print(f"Request: {i} is {'not ' if not lb.is_req_allowed() else ''}allowed, time elasped: {(i-1)*0.4}")
        sleep(0.4)
