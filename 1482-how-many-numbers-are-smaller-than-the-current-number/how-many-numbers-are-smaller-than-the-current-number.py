class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums =sorted(nums)
        ans = []
        for val in nums:
            ans.append(sorted_nums.index(val))
        return ans
