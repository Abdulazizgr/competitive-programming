class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                count += 1
                if count == k:
                    return arr[i]
        return ""
           
