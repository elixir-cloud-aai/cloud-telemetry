"""Entry point for cloud_telemetry."""

import logging

from starlette.applications import Starlette

from cloud_telemetry.middleware import OpenTelemetryInstrumentor

logger = logging.getLogger(__name__)


def init_middleware(
    app: Starlette,
    service_name: str = "ga4gh",
    enable_tracing: bool | None = None,
    enable_metrics: bool | None = None,
):
    """Initialize OpenTelemetry middleware for the Starlette application.

    Args:
        app: The Starlette application instance to instrument.
        service_name: The name of the service for tracing.
        enable_tracing: Whether to enable tracing. Default is True.
        enable_metrics: Whether to enable metrics. Default is True.

    Raises:
        Exception: If there is an error setting up tracing or metrics providers.
    """
    try:
        OpenTelemetryInstrumentor.instrument_app(
            app, service_name, enable_tracing, enable_metrics
        )
    except Exception as e:
        # Handle the exception as necessary
        logger.error(f"Failed to instrument the app with OpenTelemetry: {e}")


def main():
    """Main entry point for cloud_telemetry."""
    print("Hello from cloud_telemetry!")


if __name__ == "__main__":
    main()
