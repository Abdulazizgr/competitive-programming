class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
      

        for i in range(len(nums)):
            num = int(str(nums[i])[::-1])
            nums.append(num)

        return (len(list(set(nums))))

        