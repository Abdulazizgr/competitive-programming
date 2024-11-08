class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate_subsets(nums):
            subsets = [[]]
            
            for num in nums:
 
                subsets += [current + [num] for current in subsets]
            
            return subsets
        ans = generate_subsets(nums)
        return ans
        