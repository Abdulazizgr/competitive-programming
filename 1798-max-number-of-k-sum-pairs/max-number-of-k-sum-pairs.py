class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        end = len(nums) -1 
        start = 0
        count = 0

        while (start < end ):
            if nums[start] + nums[end] == k:
                count += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            else:
                end -=1
        return count