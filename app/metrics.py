from prometheus_client import Counter, Histogram

# Total de buscas
search_requests_total = Counter(
    "search_requests_total",
    "Total de buscas realizadas",
    ["algorithm", "found"]
)

# Tempo de execução
search_duration_ms = Histogram(
    "search_duration_ms",
    "Tempo de execução da busca em ms",
    ["algorithm", "found"]
)