class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])
        l  = 0 
        arr.sort()
        for r in range(1,len(nums)):
            if arr[r][0] != arr[l][0]:
                l = r
            else:
                while arr[r][0] == arr[l][0] and l < r:
                    if abs(arr[r][1] - arr[l][1]) <= k:
                        return True
                    l += 1        
        return False