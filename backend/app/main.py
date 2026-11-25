from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Local Retrieval-Augmented Generation (RAG) Document Assistant API",
)

# Configure CORS so the Next.js frontend can communicate with FastAPI
origins = [origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(health.router, prefix=settings.API_V1_PREFIX, tags=["Health"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME} API. Visit /docs for Swagger UI."}