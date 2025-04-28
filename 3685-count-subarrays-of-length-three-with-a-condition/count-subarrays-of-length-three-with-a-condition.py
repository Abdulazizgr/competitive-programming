class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        one = 0
        count = 0
        while one < len(nums)-2:
            if (nums[one] + nums[one+2] )== (nums[one+1] / 2):
                count += 1
            one += 1
        return count