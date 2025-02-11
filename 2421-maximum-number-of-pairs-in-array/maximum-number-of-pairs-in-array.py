class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pairs = 0
        left = 0
        print(freq)
        for value in freq.values():
            if value % 2  == 0:
                pairs += value // 2
            elif value < 2:
                left += 1
            else:
                pairs += value //2
                left += 1
        return [pairs,left]
