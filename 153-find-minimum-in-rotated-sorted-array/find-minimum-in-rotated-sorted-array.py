class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) -1
        ans = nums[0]
        while low <= high:
            mid = (low + high) // 2
            if ans > nums[mid]:
                ans = nums[mid]

            if nums[mid] > nums[high]:
                low = mid + 1
    
            else:
                high = mid -1
        return ans
             