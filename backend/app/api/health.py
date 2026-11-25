from fastapi import APIRouter
import httpx
from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check():
    """Check backend status and verify connectivity to the local Ollama service."""
    ollama_status = "unreachable"
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(f"{settings.OLLAMA_BASE_URL}/api/tags")
            if response.status_code == 200:
                ollama_status = "connected"
    except Exception:
        ollama_status = "unreachable"

    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "ollama_status": ollama_status,
        "configured_model": settings.OLLAMA_MODEL,
    }