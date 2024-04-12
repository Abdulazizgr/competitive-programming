

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 1
        maxsum = nums[0]
        lis = [nums[0]]
        
        while right < len(nums):
            if nums[right] in lis:
                maxsum = max(maxsum, sum(lis))
                while nums[left] != nums[right]:
                    lis.remove(nums[left])
                    left += 1
                left += 1
            else:
                lis.append(nums[right])
            right += 1
        
        maxsum = max(maxsum, sum(lis))
        return maxsum