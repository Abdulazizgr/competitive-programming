class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [key  for key,value in cnt.items() if value == 2]
        