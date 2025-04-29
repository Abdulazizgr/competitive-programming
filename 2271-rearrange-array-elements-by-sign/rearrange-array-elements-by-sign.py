class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = []
        negative_nums = []

        for num in nums:
            if num > 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)

        result = []
        i = 0
        while i < len(positive_nums):
            result.append(positive_nums[i])
            result.append(negative_nums[i])
            i += 1

        return result
