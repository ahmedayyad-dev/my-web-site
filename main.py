import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from app.api import router as api_router

# Initialize FastAPI app
app = FastAPI(
    title="Ahmed Ayyad Portfolio API",
    description="Professional portfolio backend with FastAPI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Compression
app.add_middleware(GZipMiddleware, minimum_size=1000)


# No-Cache Middleware (only for static files)
class NoCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        # Only apply no-cache to HTML files
        if request.url.path.endswith('.html') or request.url.path == '/':
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
        return response


app.add_middleware(NoCacheMiddleware)

# Include API router
app.include_router(api_router)


# Root endpoint
@app.get("/api")
async def api_root():
    return {
        "message": "Ahmed Ayyad Portfolio API",
        "version": "1.0.0",
        "endpoints": {
            "portfolio": "/api/v1/portfolio",
            "profile": "/api/v1/profile",
            "skills": "/api/v1/skills",
            "social_links": "/api/v1/social-links",
            "about": "/api/v1/about",
            "contact": "/api/v1/contact",
            "stats": "/api/v1/stats",
            "health": "/api/v1/health",
            "docs": "/api/docs"
        }
    }


# 404 Handler - Redirect to home
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Redirect any 404 to home page"""
    return RedirectResponse(url="/", status_code=302)


# Mount static files (frontend) - must be last
app.mount("/", StaticFiles(directory="ahmedayyad.dev", html=True), name="static")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 2200)),
        reload=True  # Enable auto-reload in development
    )
