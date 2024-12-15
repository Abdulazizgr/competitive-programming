class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = []
        # print(nums)


        while left < right :
            a = nums[left] + nums[right]
            a = a / 2
            print(a)
            ans.append(a)

            left += 1
            right -= 1
        ans.sort()
        # print(ans)
        return ans[0]
