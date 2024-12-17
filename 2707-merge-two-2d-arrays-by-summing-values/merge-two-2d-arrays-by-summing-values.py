class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        fir = 0
        sec = 0
        ans = []

        while fir < len(nums1) and sec < len(nums2):
            if nums1[fir][0] == nums2[sec][0]:
                ans.append([nums1[fir][0],nums1[fir][1] + nums2[sec][1]])
                fir += 1
                sec += 1
            elif nums1[fir][0] < nums2[sec][0]:
                ans.append(nums1[fir])
                fir += 1
            elif nums1[fir][0] > nums2[sec][0]:
                ans.append(nums2[sec])
                sec += 1
        ans.extend(nums1[fir:])
        ans.extend(nums2[sec:])

        return ans
