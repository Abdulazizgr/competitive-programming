class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == nums.count(0):
            return str(nums[0])
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse= True)
        # srt = srt[::-1]
        print(nums)
        res=""
        for i in nums:
            res += str(i)
        return res 