class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        for i in range(len(nums2)):
            nums2[i]=nums2[i]*k
        
        cnt=0
        for i in nums1:
            for j in nums2:
                if i%j==0:
                    cnt+=1
        return cnt