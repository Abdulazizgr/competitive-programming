class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_index = []
        nums.sort()
        for index, val  in enumerate(nums):
            if val == target:
                target_index.append(index)
        

        return target_index