class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        idx = 0
        for row in mat:
            one = row.count(1)
            count.append([one,idx])
            idx += 1
        count.sort(key=lambda x: (x[0], x[1]))

        res = []
        for idx in range(k):
            res.append(count[idx][1])
        return res
