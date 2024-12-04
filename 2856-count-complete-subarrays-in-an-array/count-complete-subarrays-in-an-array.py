class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        count = Counter()
        ans = 0 
        i =0
        for j in nums:
            count[j] += 1
           
            while len(count) == n:
                left = nums[i]
                count[left] -= 1
                if count[left] == 0: 
                    del count[left]
                i+= 1
            ans+= i
        return ans