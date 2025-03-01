class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        nums.sort()
        left = 0 
        right = len(nums) -1

        while left< right:
            key = (nums[left] + nums[right]) / 2
            ans[key] += 1
            left += 1
            right -= 1

        return len(ans)