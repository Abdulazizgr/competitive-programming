class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pep = list(zip(names, heights))
        pep.sort(key=lambda x: x[1], reverse=True)
        return [i for i, _ in pep]