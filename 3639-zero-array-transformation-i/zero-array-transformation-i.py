class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        nums1 = [0] * (len(nums))
        for start,end in queries:
            nums1[start] -= 1
            if end + 1 < len(nums):
                nums1[end + 1] += 1
        nums1 = list(accumulate(nums1))

        
        for idx in range(len(nums)):
            if nums[idx] + nums1[idx] > 0:
                return False

        return True
    

