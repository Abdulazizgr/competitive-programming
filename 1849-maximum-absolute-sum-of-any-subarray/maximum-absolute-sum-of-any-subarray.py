class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        ans = max(0,max(prefix_sum)) - min(0,min(prefix_sum))

        return ans