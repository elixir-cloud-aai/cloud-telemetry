"""Entry point for cloud_telemetry."""

from starlette.applications import Starlette

from cloud_telemetry.middleware import OpenTelemetryInstrumentor


def init_middleware(app: Starlette):
    """Initialize middleware for the Starlette application.

    Args:
        app (Starlette): The Starlette application instance to instrument.

    Raises:
        ValueError: If the application instance is not provided or is invalid.
    """
    try:
        OpenTelemetryInstrumentor.instrument_app(app, service_name="ga4gh")

    except Exception as e:
        # Log the exception or handle it as necessary
        print(f"Failed to instrument the app with OpenTelemetry: {e}")


def main():
    """Main entry point for cloud_telemetry."""
    print("Hello from cloud_telemetry!")


if __name__ == "__main__":
    main()
