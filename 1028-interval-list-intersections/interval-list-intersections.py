class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        ans = []

        while p1 < len(firstList) and p2 < len(secondList):
            a, b = firstList[p1]
            c, d = secondList[p2]

            start = max(a, c)
            end = min(b, d)

            if start <= end:
                ans.append([start, end])
            if b < d:
                p1 += 1
            else:
                p2 += 1

        return ans
