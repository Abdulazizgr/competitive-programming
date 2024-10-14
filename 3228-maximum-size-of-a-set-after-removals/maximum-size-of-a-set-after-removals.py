class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        n = len(nums1)
        inter = s1 & s2
        ex1 = min(len(s1) - len(inter) , n//2)
        ex2 = min(len(s2) - len(inter) , n//2)
        return (min(ex1 + ex2 + len(inter) , n))