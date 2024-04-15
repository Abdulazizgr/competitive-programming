class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = nums.count(min(nums))
        if n == len(nums):
            return 0 
        lar = nums[0]
        count = 0
        for i in range(1,len(nums)):
            if lar > nums[i]:
                count += i
                lar = nums[i]
        
        return count