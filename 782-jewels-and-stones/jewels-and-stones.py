class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        count =0
        for i in range(len(stones)):
            if stones[i] in j:
                count += 1
        return count
