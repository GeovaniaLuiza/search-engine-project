import time
from .base import SearchStrategy, SearchResult

class RabinKarpSearch(SearchStrategy):
    def search(self, text, pattern):
        start = time.time()

        d = 256
        q = 101
        m = len(pattern)
        n = len(text)

        h = pow(d, m-1) % q
        p = t = 0
        positions = []

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for i in range(n - m + 1):
            if p == t:
                if text[i:i+m] == pattern:
                    positions.append(i)

            if i < n - m:
                t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
                if t < 0:
                    t += q

        end = time.time()
        return SearchResult(positions, (end - start) * 1000)