class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        le = []
       
        gr = []
    

        for i in range(len(nums)):
            if nums[i] > pivot:
               gr.append(nums[i])
            elif nums[i] < pivot:
                le.append(nums[i])
        n = len(nums) - len(le) - len(gr)
        return le + [pivot]*n + gr