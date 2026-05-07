from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader

# TRACES
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# METRICS
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter(__name__)

search_duration = meter.create_histogram(
    name="search_duration_ms",
    description="Tempo de busca",
)

search_counter = meter.create_counter(
    name="search_requests_total"
)