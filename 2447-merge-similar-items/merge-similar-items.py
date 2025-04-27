class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        for value,weight in items1:
            count[value] += weight
        for value,weight in items2:
            count[value] += weight
        res = [[key,value] for key,value in count.items()]
        res.sort()
        return res