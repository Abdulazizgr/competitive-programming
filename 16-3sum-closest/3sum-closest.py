class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        num = 0
        diff = float('inf')

        for i in range(len(nums)-2):  
            left = i + 1  
            right = len(nums) - 1

            while left < right:
                _sum = nums[left] + nums[right] + nums[i]
                
                if _sum == target:
                    return _sum
                
                if diff > abs(target - _sum):
                    diff = abs(target - _sum)
                    num = _sum

                if _sum > target:
                    right -= 1
                else:
                    left += 1

        return num
