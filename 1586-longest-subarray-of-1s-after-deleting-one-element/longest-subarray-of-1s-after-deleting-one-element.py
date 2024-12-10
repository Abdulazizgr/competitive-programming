class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        count = 0

        for end in range(len(nums)):

            if nums[end] == 0:
                count += 1
            while count > 1:
                if nums[s] == 0:
                    count -= 1
                s +=1
            ans = max(ans,end - s)
        return ans
        