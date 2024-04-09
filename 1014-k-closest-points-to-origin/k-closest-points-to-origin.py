class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = 0
        result = {}
        for i in range(len(points)):
            ele = points[i]

            ans = sqrt(ele[0]**2 + (ele[1]**2))
            result[i] = ans

        sorted_dict = dict(sorted(result.items(), key=lambda x: x[1]))
        sorted_keys = list(sorted_dict.keys())[:k]
        return [points[i] for i in sorted_keys]