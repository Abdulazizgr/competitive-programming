class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:
                a = (i+nums[i] ) % len(nums)
                ans.append(nums[a])
            elif nums[i] < 0:
                a = (i-abs(nums[i])) %len(nums)
                ans.append(nums[a])
            else:
                ans.append(nums[i])
        return ans
