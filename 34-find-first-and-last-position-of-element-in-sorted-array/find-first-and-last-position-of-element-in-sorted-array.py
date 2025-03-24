class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftOccurrence():
            left = -1
            low = 0
            high = len(nums) -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    left = mid
                    high = mid -1
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return left
        def rightOccurrence():
            right = -1
            low = 0
            high = len(nums) -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    right = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return right
        return [leftOccurrence(),rightOccurrence()]