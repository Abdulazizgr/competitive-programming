class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pref_sum[i+1] = pref_sum[i] + nums[i]
    

        for idx in range(1,len(pref_sum)):
            if pref_sum[idx-1] == ( pref_sum[-1] - pref_sum[idx]) :
                return idx -1
        return -1
