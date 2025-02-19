class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_count:
                result += prefix_count[prefix_sum-goal]
            prefix_count[prefix_sum] += 1
        return result
            
            