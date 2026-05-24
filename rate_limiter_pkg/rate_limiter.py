from abc import ABC, abstractmethod


class RateLimiter(ABC):

    @abstractmethod
    def is_req_allowed(self) -> bool:
        pass
