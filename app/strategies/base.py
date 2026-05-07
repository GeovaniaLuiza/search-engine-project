from abc import ABC, abstractmethod
from typing import List

class SearchResult:
    def __init__(self, positions: List[int], time_ms: float):
        self.positions = positions
        self.occurrences = len(positions)
        self.time_ms = time_ms
        self.found = self.occurrences > 0

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, text: str, pattern: str) -> SearchResult:
        pass