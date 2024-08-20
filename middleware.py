from opentelemetry.instrumentation.starlette import StarletteInstrumentor
from starlette.applications import Starlette
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
# from prometheus_client import start_http_server

class OpenTelemetryInstrumentor():
    """Instrument a Starlette application with OpenTelemetry."""

    def instrument_app(
        app: Starlette,
        service_name: str = "ga4gh",
    ):
        resource = Resource(attributes={
            SERVICE_NAME: service_name
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

        StarletteInstrumentor().instrument_app(app)

                
