import copy
import random
import math

from nltk import Tree

from schemas.paraphrasing_schemas import TreeParaphraseList, TreeParaphrase


class TreeParaphrasingService:
    def __init__(self, tree: str):
        self.tree = Tree.fromstring(tree)

    def count_permutations(self, tree: list[Tree]) -> int:
        if len(tree) == 0 or tree[0].height() <= 3:
            return 1

        if tree[0].label() == "NP":
            num_nps = sum(1 for child in tree[0] if child.label() == "NP")
            if num_nps >= 2:
                return math.factorial(num_nps) * self.count_permutations([tree[0][0]])

        left_count = self.count_permutations([tree[0]])
        right_count = self.count_permutations(tree[1:])

        return left_count * right_count

    def shuffle_nps(self, tree: Tree) -> None:
        # check for trees with no children or leaves only
        if tree.height() < 3:
            return

        if tree.label() == "NP":
            nps = [branch for branch in tree if branch.label() == "NP"]
            if len(nps) >= 2:
                random.shuffle(nps)
                for i, val in enumerate(tree):
                    if val.label() == "NP":
                        tree[i] = nps.pop()

        for child in tree:
            self.shuffle_nps(child)

    def find_permutations(self) -> list[str]:
        permutations = set()

        num_permutations = self.count_permutations(tree=list(self.tree))
        while len(permutations) < num_permutations:
            new_tree = copy.deepcopy(self.tree)
            self.shuffle_nps(new_tree)
            new_permutation = " ".join(str(new_tree).split())
            permutations.add(new_permutation)

        return list(permutations)

    def paraphrase_syntactic_tree(self, limit: int) -> TreeParaphraseList:
        paraphrases = self.find_permutations()[:limit]
        results = [TreeParaphrase(tree=paraphrase) for paraphrase in paraphrases]

        return TreeParaphraseList(paraphrases=results)
