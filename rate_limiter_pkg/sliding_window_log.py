from time import time, sleep
from rate_limiter_pkg.rate_limiter import RateLimiter


class SlidingWindowLog(RateLimiter):

    def __init__(self, allowed_req_count: int, window_size: int):

        self.allowed_req_count = allowed_req_count
        self.window_size = window_size
        self.log = []

    def is_req_allowed(self) -> bool:

        now = time()

        # remove expired timestamps
        self.log = [tp for tp in self.log if tp >= now - self.window_size]

        # reject if limit exceeded
        if len(self.log) >= self.allowed_req_count:
            return False

        # accept request
        self.log.append(now)

        return True


if __name__ == "__main__":
    swl = SlidingWindowLog(allowed_req_count=4, window_size=6)
    for i in range(1, 9):
        print(f"Request: {i} is {'not ' if not swl.is_req_allowed() else ''}allowed, time elasped: {i-1}")
        sleep(1)
