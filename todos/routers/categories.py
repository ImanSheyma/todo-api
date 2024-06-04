from fastapi import APIRouter

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)

@router.get('/')
async def get_categories():
    return 'categories'

@router.post('/')
async def create_category():
    return 'new category'

@router.put('/')
async def update_category():
    return 'updated category'

@router.get('/')
async def delete_category():
    return 'deleted category'