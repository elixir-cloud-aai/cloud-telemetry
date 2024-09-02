"""Entry point for cloud_telemetry."""

from starlette.applications import Starlette

from cloud_telemetry.middleware import OpenTelemetryInstrumentor


def init_middleware(app: Starlette, service_name: str = "ga4gh"):
    """Initialize OpenTelemetry middleware for the Starlette application.

    Args:
        app (Starlette): The Starlette application instance to instrument.
        service_name (str): The name of the service for tracing.

    Raises:
        Exception: If there is an error setting up tracing or metrics providers.
    """
    try:
        OpenTelemetryInstrumentor.instrument_app(app, service_name)
    except Exception as e:
        # Handle the exception as necessary
        print(f"Failed to instrument the app with OpenTelemetry: {e}")


def main():
    """Main entry point for cloud_telemetry."""
    print("Hello from cloud_telemetry!")


if __name__ == "__main__":
    main()
