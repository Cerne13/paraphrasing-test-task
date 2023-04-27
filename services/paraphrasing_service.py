from nltk import Tree

from schemas.paraphrasing_schemas import TreeParaphraseList, TreeParaphrase


class TreeParaphrasingService:
    def __init__(self, tree: str):
        self.tree = Tree.fromstring(tree)

    def paraphrase_syntactic_tree(self, limit: int) -> TreeParaphraseList:
        print(limit)
        return TreeParaphraseList(
            paraphrases=[
                TreeParaphrase(tree='one'),
                TreeParaphrase(tree='two')
            ]
        )
