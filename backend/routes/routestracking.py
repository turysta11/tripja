from fastapi import APIRouter
router = APIRouter()

@router.get("/tracking")
def get_tracking():
    ...
