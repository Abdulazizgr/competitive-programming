class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        pointer = 0
        while pointer < len(nums):
            idx = nums[pointer] - 1
            if nums[pointer] != nums[idx]:
                nums[pointer], nums[idx] = nums[idx], nums[pointer]
            else:
                pointer += 1
        for idx in range(len(nums)):
            if nums[idx] - 1 != idx:
                return [nums[idx],idx+1]