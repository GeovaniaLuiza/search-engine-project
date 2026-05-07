import time
from .base import SearchStrategy, SearchResult

class BoyerMooreSearch(SearchStrategy):

    def bad_character_heuristic(self, pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    def search(self, text, pattern):
        start = time.time()

        m = len(pattern)
        n = len(text)

        bad_char = self.bad_character_heuristic(pattern)

        positions = []
        s = 0

        while s <= n - m:
            j = m - 1

            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                positions.append(s)
                s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
            else:
                s += max(1, j - bad_char.get(text[s + j], -1))

        end = time.time()
        return SearchResult(positions, (end - start) * 1000)