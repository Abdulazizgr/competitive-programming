class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        sm = 0
        ans = 0
        for i in range(len(nums)):
            sm += nums[i]

            if sm-goal in mp:
                ans += mp[sm-goal]
            # print(mp)
            
            mp[sm] += 1
        
        return ans

        # def compute(k):
        #     left = right = 0
        #     ans = 0
        #     sm = 0
        #     while right < len(nums):
        #         sm += nums[right]
        #         while sm > k and left <= right:
        #             sm -= nums[left]
        #             left += 1

        #         ans += (right - left + 1)
        #         right += 1
        #     return ans
        
        # return compute(goal) - compute(goal-1)
