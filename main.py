from opentelemetry.instrumentation.starlette import StarletteInstrumentor
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
# from prometheus_client import start_http_server
import asyncio
import random

# from opentelemetry.exporter.prometheus import PrometheusMetricReader

resource = Resource(attributes={
    SERVICE_NAME: "testing-ga4gh"
})

# Traces : Console
# traceProvider = TracerProvider(resource=resource)
# processor = BatchSpanProcessor(ConsoleSpanExporter())
# traceProvider.add_span_processor(processor)
# trace.set_tracer_provider(traceProvider)

# Jaeger || otel col setup : Exposing OTLP traces
# more read here: https://medium.com/jaegertracing/introducing-native-support-for-opentelemetry-in-jaeger-eb661be8183c
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter())
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

# prometheus || otel col setup : Exposing OTLP metrics

from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
reader = PeriodicExportingMetricReader(OTLPMetricExporter())
meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meterProvider)

# Prometheus : Console

# reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
# meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
# metrics.set_meter_provider(meterProvider)
# Start Prometheus client

# Prometheus : HTTP

# start_http_server(port=9464, addr="localhost")
# Initialize PrometheusMetricReader which pulls metrics from the SDK
# on-demand to respond to scrape requests

# reader = PrometheusMetricReader()
# meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
# metrics.set_meter_provider(meterProvider)

# Testing APIs

async def home(request):
    return JSONResponse("hi")

async def process_data(request):
    await asyncio.sleep(random.uniform(1, 3))
    return JSONResponse({"status": "Data processed successfully"})

async def generate_report(request):
    await asyncio.sleep(random.uniform(2, 5))
    return JSONResponse({"status": "Report generated successfully"})

async def perform_analysis(request):
    await asyncio.sleep(random.uniform(3, 7))
    return JSONResponse({"status": "Analysis completed"})

async def backup_database(request):
    await asyncio.sleep(random.uniform(5, 10))
    return JSONResponse({"status": "Database backup completed"})

async def optimize_system(request):
    await asyncio.sleep(random.uniform(4, 8))
    return JSONResponse({"status": "System optimization completed"})

async def send_notifications(request):
    await asyncio.sleep(random.uniform(1, 4))
    return JSONResponse({"status": "Notifications sent successfully"})

app = Starlette(
    routes=[
        Route("/", home),
        Route("/process-data", process_data),
        Route("/generate-report", generate_report),
        Route("/perform-analysis", perform_analysis),
        Route("/backup-database", backup_database),
        Route("/optimize-system", optimize_system),
        Route("/send-notifications", send_notifications),
    ]
)

# Instrument the application
StarletteInstrumentor.instrument_app(app)
