class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = Counter(nums1)
        num2 = Counter(nums2)
        ans1 = []
        ans2 = []
        for key,value in num1.items():
            if  key not  in num2:
                ans1.append(key)
        for key,value in num2.items():
            if  key not  in num1:
                ans2.append(key)
        return [ans1,ans2]