class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0,0
        while right < len(nums) and left < len(nums):
            if nums[left] != 0 and left < right:
                left += 1
            else:
                if nums[right] == 0:
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right += 1
                    left += 1
        