class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = {}
        for index, num in enumerate(nums):
            if target - num in cnt:
                return [cnt[target - num],index]
            
            cnt[num] = index
        