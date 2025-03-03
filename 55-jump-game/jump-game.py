class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        max_reach = 0
        for idx in range(n):
            if idx > max_reach:
                return False
            max_reach = max(max_reach, idx + nums[idx])
            if max_reach >= n - 1:
                return True
        return True