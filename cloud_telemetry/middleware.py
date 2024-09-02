"""Middleware for OpenTelemetry instrumentation."""

from opentelemetry import metrics, trace
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.starlette import StarletteInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from starlette.applications import Starlette


class OpenTelemetryInstrumentor:
    """Instruments a Starlette application with OpenTelemetry."""

    @staticmethod
    def instrument_app(
        app: Starlette,
        service_name: str = "ga4gh",
    ):
        """Instruments a Starlette application with OpenTelemetry.

        Args:
            app (Starlette): The Starlette application instance to be instrumented.
            service_name (str): The name of the service for tracing and metrics.
            Default is "ga4gh".

        Raises:
            ValueError: If the provided app is not a Starlette instance.
            RuntimeError: If there is an error setting up tracing or metrics providers.
        """
        try:
            # Set up OpenTelemetry resource with the service name.
            resource = Resource(attributes={SERVICE_NAME: service_name})

            # Set up the trace provider and exporter for sending trace data.
            trace_provider = TracerProvider(resource=resource)
            span_processor = BatchSpanProcessor(
                OTLPSpanExporter()
            )  # Exporter for traces.
            trace_provider.add_span_processor(span_processor)
            trace.set_tracer_provider(trace_provider)  # Set the global tracer provider.

            # Set up the metric provider and exporter for sending metric data.
            metric_reader = PeriodicExportingMetricReader(
                OTLPMetricExporter()
            )  # Exporter for metrics.
            meter_provider = MeterProvider(
                resource=resource, metric_readers=[metric_reader]
            )
            metrics.set_meter_provider(meter_provider)  # Set the global meter provider.

            # Instrument the Starlette app with the configured tracing and metrics.
            StarletteInstrumentor().instrument_app(app)

        except Exception as e:
            # Raise an exception with a descriptive error message
            # if instrumentation fails.
            raise RuntimeError(f"Failed to instrument the Starlette app: {e}") from e
