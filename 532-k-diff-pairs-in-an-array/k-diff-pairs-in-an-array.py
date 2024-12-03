class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0
        for num in nums:
            dic[num] += 1
        if k == 0:
            for num in dic:
                if dic[num] > 1:
                    count += 1
        else:
            for num in dic:
                if num + k in dic:
                    count += 1
        return count
