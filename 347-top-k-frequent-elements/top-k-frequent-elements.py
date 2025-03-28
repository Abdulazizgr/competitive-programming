class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        ans = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans