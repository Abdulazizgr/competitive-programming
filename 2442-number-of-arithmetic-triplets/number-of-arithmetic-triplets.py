class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] + diff in nums:
                a = nums[i] + diff
                if a + diff in nums:
                    count += 1
        return count