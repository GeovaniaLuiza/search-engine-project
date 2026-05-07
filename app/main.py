from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

from app.strategies.naive import NaiveSearch
from app.strategies.kmp import KMPSearch
from app.strategies.rabin_karp import RabinKarpSearch
from app.strategies.boyer_moore import BoyerMooreSearch

from app.metrics import search_requests_total, search_duration_ms

import time
import logging

# OpenTelemetry (se você estiver usando)
from app.telemetry import tracer

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

strategies = {
    "naive": NaiveSearch(),
    "kmp": KMPSearch(),
    "rabin": RabinKarpSearch(),
    "bm": BoyerMooreSearch()
}

@app.post("/search")
async def search(file: UploadFile, pattern: str = Form(...), algorithm: str = Form(...)):

    with tracer.start_as_current_span("search_request"):

        # leitura
        with tracer.start_as_current_span("read_file"):
            content = await file.read()
            text = content.decode("utf-8")

        if not text:
            return {"error": "Arquivo vazio"}

        strategy = strategies.get(algorithm)

        if not strategy:
            return {
                "error": "Algoritmo inválido",
                "available": list(strategies.keys())
            }

        N = len(text)
        M = len(pattern)

        logging.info(f"Iniciando busca | algoritmo={algorithm} N={N} M={M}")

        # execução
        with tracer.start_as_current_span("execute_algorithm"):
            start = time.time()
            result = strategy.search(text, pattern)
            duration = (time.time() - start) * 1000

        # 📊 MÉTRICAS CORRETAS (PROMETHEUS)
        search_requests_total.labels(
            algorithm=algorithm,
            found=str(result.found)
        ).inc()

        search_duration_ms.labels(
            algorithm=algorithm,
            found=str(result.found)
        ).observe(duration)

        logging.info(
            f"Finalizado | tempo={duration:.2f}ms ocorrencias={result.occurrences}"
        )

        # resposta
        with tracer.start_as_current_span("format_response"):
            return {
                "found": result.found,
                "occurrences": result.occurrences,
                "positions": result.positions,
                "time_ms": duration,
                "N": N,
                "M": M
            }

# 📊 MÉTRICAS ENDPOINT
@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )