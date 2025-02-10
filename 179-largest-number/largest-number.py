class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if nums.count(0) == n:
            return "0"
        for i in range(n):
            nums[i] = str(nums[i])
    
        for i in range(n):
            for j in range(i + 1, n):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
         
        return "".join(nums)






        