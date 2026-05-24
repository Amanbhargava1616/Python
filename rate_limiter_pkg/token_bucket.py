from time import time, sleep
from rate_limiter_pkg.rate_limiter import RateLimiter


class TokenBucket(RateLimiter):
    def __init__(self, capacity: int, refill_rate: int) -> None:

        self.capacity: int = capacity
        self.token: int = capacity
        self.refill_rate: int = refill_rate
        self.last_refiled_time: float = time()

    def is_req_allowed(self) -> bool:

        now: float = time()
        if now - self.last_refiled_time >= self.refill_rate:
            self.token = self.capacity
            self.last_refiled_time = now

        self.token -= 1
        if self.token < 0:
            return False
        return True


if __name__ == "__main__":
    tb = TokenBucket(capacity=4, refill_rate=6)
    for i in range(1, 9):
        print(f"Request: {i} is {'not ' if not tb.is_req_allowed() else ''}allowed, time elasped: {i-1}")
        sleep(1)
