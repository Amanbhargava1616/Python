from time import time, sleep
from rate_limiter_pkg.rate_limiter import RateLimiter


class FixedWindowCounter(RateLimiter):

    def __init__(self, allowed_req_count: int, window_size: int) -> None:

        self.allowed_req_count = allowed_req_count
        self.counter = 0
        self.window_start = time()
        self.window_size = window_size

    def is_req_allowed(self) -> bool:

        now = time()

        # new window starts
        if now - self.window_start >= self.window_size:
            self.counter = 0
            self.window_start = now

        # reject if limit reached
        if self.counter >= self.allowed_req_count:
            return False

        # accept request
        self.counter += 1

        return True


if __name__ == "__main__":
    fwc = FixedWindowCounter(allowed_req_count=4, window_size=6)
    for i in range(1, 9):
        print(f"Request: {i} is {'not ' if not fwc.is_req_allowed() else ''}allowed, time elasped: {i-1}")
        sleep(1)
