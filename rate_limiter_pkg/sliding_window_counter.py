from time import time, sleep
from rate_limiter_pkg.rate_limiter import RateLimiter


class SlidingWindowCounter(RateLimiter):

    def __init__(self, allowed_req_count: int, window_size: int) -> None:

        self.allowed_req_count = allowed_req_count
        self.window_size = window_size

        self.current_window_count = 0
        self.previous_window_count = 0

        self.window_start = time()

    def is_req_allowed(self) -> bool:

        now = time()
        elapsed = now - self.window_start

        # move to next window
        if elapsed >= self.window_size:

            self.previous_window_count = self.current_window_count
            self.current_window_count = 0

            self.window_start = now
            elapsed = 0

        # weighted previous window contribution
        weighted_previous_count = (1 - elapsed / self.window_size) * self.previous_window_count

        # estimated request count
        estimated_count = weighted_previous_count + self.current_window_count

        # reject if limit exceeded
        if estimated_count >= self.allowed_req_count:
            return False

        # accept request
        self.current_window_count += 1

        return True


if __name__ == "__main__":
    swc = SlidingWindowCounter(allowed_req_count=4, window_size=6)
    for i in range(1, 9):
        print(f"Request: {i} is {'not ' if not swc.is_req_allowed() else ''}allowed, time elasped: {i-1}")
        sleep(1)
