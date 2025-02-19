class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_min = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum,prefix_sum-curr_min)
            if prefix_sum < curr_min:
                curr_min = prefix_sum

        return max_sum