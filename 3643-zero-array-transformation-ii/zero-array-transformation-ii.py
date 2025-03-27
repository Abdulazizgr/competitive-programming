class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isValid(mid):
            nums1 = [0] * (len(nums))
            for start,end,val in queries[:mid]:
                nums1[start] -= val
                if end + 1 < len(nums):
                    nums1[end + 1] += val
            nums1 = list(accumulate(nums1))
            for idx in range(len(nums)):
                if nums[idx] + nums1[idx] > 0:
                    return False

            return True


        low = 0
        high = len(queries) 
        ans = high + 1

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        if ans <= len(queries):
            return ans
        return -1