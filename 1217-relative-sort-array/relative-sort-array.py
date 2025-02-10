class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        freq = Counter(arr1)

        for num in arr2:
            result.extend([num] * freq.pop(num, 0))

        result.extend(sorted(freq.elements()))
        return result
