import copy
import random
import math

from fastapi import HTTPException
from nltk.tree import Tree

from schemas.paraphrasing_schemas import TreeParaphraseList, TreeParaphrase


class TreeParaphrasingService:
    def __init__(self, tree_str: str):
        self.tree = Tree.fromstring(tree_str)

    def count_tree_permutations(self, tree: Tree) -> int:
        if tree.height() <= 3:
            return 1

        counter = sum([1 for elem in tree if elem.label() == "NP"])
        if counter >= 2:
            return math.factorial(counter) * math.prod(
                self.count_tree_permutations(elem) for elem in tree if elem.label() == "NP"
            )

        return math.prod(self.count_tree_permutations(elem) for elem in tree)

    def shuffle_np_subtrees(self, tree: Tree) -> None:
        # check for trees with no children or leaves only
        if tree.height() < 3:
            return

        if tree.label() == "NP":
            np_subtrees = [branch for branch in tree if branch.label() == "NP"]

            if len(np_subtrees) >= 2:
                labels = [child.label() for child in tree[0:]]

                if labels.count('NP') >= 2 and ('CC' in labels or ',' in labels):
                    random.shuffle(np_subtrees)
                    for i, val in enumerate(tree):
                        if val.label() == "NP":
                            tree[i] = np_subtrees.pop()

        for child in tree:
            self.shuffle_np_subtrees(child)

    def find_all_tree_permutations(self) -> list[str]:
        tree_permutations = set()

        num_permutations = self.count_tree_permutations(tree=self.tree)
        while len(tree_permutations) < num_permutations:
            new_tree = copy.deepcopy(self.tree)
            self.shuffle_np_subtrees(new_tree)

            new_permutation = " ".join(str(new_tree).split())
            tree_permutations.add(new_permutation)

        return list(tree_permutations)

    def paraphrase_syntactic_tree(self, limit: int) -> TreeParaphraseList:
        tree_permutations = self.find_all_tree_permutations()[:limit]

        if not tree_permutations:
            raise HTTPException(status_code=404, detail='No paraphrases exist for this tree')

        paraphrase_results = [TreeParaphrase(tree=tree_permutation) for tree_permutation in tree_permutations]
        return TreeParaphraseList(paraphrases=paraphrase_results)
