class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for i in freq:
            if i + 1 in freq:
                ans = max(ans,freq[i]+freq[i+1])
        return ans