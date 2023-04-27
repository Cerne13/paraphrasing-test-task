from typing import List
from pydantic import BaseModel


class TreeParaphrase(BaseModel):
    tree: str


class TreeParaphraseList(BaseModel):
    paraphrases: List[TreeParaphrase]
