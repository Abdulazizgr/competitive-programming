class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minimum = abs(min(nums))
        maximum = max(nums)
        ans = []

        counts = [0] * (maximum + minimum + 1)
        for num in nums:
            counts[num + minimum] += 1
       
        for index,value in enumerate(counts):
            if value > 0:
                ans.extend([index-minimum] * value)

        return ans

