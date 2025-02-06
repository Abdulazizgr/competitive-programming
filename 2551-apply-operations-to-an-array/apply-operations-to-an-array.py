class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index + 1] = 0
        zeros = nums.count(0)
        for val in nums:
            if val != 0:
                ans.append(val)
        for i in range(zeros):
            ans.append(0)
        return ans