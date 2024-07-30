from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import asyncio
import random
from middleware import OpenTelemetryInstrumentor

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

# Temp Routes for testing
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

OpenTelemetryInstrumentor.instrument_app(app)