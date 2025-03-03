class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for idx in range(2,len(nums)):
            if nums[idx-2] < nums[idx-1] + nums[idx]:
                return nums[idx-2] + nums[idx-1] + nums[idx]
        return 0