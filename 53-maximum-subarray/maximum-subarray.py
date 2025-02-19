class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_min = 0
        prefix_sum = [0] * (len(nums) +1)

        for i  in range(len(nums)):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]
        for i in range(1,len(prefix_sum)):
            max_sum = max(max_sum,prefix_sum[i]-curr_min)
            if prefix_sum[i] < curr_min:
                curr_min = prefix_sum[i]

        return max_sum