
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/career")
async def get_career(query: str, request: Request):
    rag_pipeline = request.app.state.rag_pipeline
    result = await rag_pipeline.run(query)
    return result
