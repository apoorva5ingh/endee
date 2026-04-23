from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import uvicorn
import logging
import os

from api.career_routes import router as career_router
from api.health_routes import router as health_router
from core.vector_store import VectorStore          # ✅ Only import the class
from core.embeddings import EmbeddingEngine
from core.rag_pipeline import RAGPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize all services on startup."""
    logger.info("🚀 Starting AI Career Engine...")

    # Initialize vector store
    app.state.vector_store = VectorStore()
    await app.state.vector_store.initialize()
    logger.info("✅ Vector Store initialized")

    # Initialize embedding engine
    app.state.embedding_engine = EmbeddingEngine()
    logger.info("✅ Embedding Engine initialized")

    # Initialize RAG pipeline
    app.state.rag_pipeline = RAGPipeline(
        vector_store=app.state.vector_store,
        embedding_engine=app.state.embedding_engine
    )
    logger.info("✅ RAG Pipeline initialized")

    yield

    logger.info("🛑 Shutting down AI Career Engine...")


app = FastAPI(
    title="AI Career Path + Job Intelligence Engine",
    description="Semantic search + RAG powered career guidance system",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# Include routers
app.include_router(career_router, prefix="/api/v1", tags=["Career Intelligence"])
app.include_router(health_router, prefix="/api/v1", tags=["Health"])


@app.get("/", include_in_schema=False)
async def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "templates", "index.html")
    return FileResponse(frontend_path)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

    from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)