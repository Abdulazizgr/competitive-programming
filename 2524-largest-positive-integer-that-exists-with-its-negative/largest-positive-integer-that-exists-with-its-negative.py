class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) -1

        while left < right:
            if nums[left] < 0:
                if nums[left] + nums[right] == 0:
                    return nums[right]
                
                elif nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            else:
                return -1
        return -1