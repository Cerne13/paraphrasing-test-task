from fastapi import APIRouter, status

from schemas.paraphrasing_schemas import TreeParaphraseList
from services.paraphrasing_service import TreeParaphrasingService

router = APIRouter(
    prefix='/paraphrase',
    tags=['paraphrase'],
    responses={
        404: {'description': 'Not found'}
    }
)


@router.get('', status_code=status.HTTP_200_OK)
async def paraphrase(tree: str, limit: int | None = 20) -> TreeParaphraseList:
    service = TreeParaphrasingService(tree_str=tree)
    result = service.paraphrase_syntactic_tree(limit)

    return result
