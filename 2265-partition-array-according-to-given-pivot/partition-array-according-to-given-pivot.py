class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        le = []
        eq = []
        gr = []
    

        for i in range(len(nums)):
            if nums[i] > pivot:
               gr.append(nums[i])
            elif nums[i] < pivot:
                le.append(nums[i])
            else:
                eq.append(nums[i])
        return le + eq + gr