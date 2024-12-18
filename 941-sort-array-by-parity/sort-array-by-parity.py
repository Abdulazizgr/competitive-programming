class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0

        while left < len(nums) and right < len(nums) :
            if nums[right] % 2 == 0:
                nums[left],nums[right] = nums[right] ,nums[left]
                left += 1
            right += 1
        return nums

        