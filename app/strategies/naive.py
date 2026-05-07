import time
from .base import SearchStrategy, SearchResult

class NaiveSearch(SearchStrategy):
    def search(self, text, pattern):
        start = time.time()
        positions = []

        for i in range(len(text) - len(pattern) + 1):
            match = True
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                positions.append(i)

        end = time.time()
        return SearchResult(positions, (end - start) * 1000)