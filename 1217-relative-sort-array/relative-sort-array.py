class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr2)):
            n = arr1.count(arr2[i])
            for j in range(n):
                ans.append(arr2[i])
                print(ans)
                arr1.remove(arr2[i])
                print(arr1)
        arr1.sort()
        return (ans+arr1)