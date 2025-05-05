from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, numbers: List[int], min_pairs: int) -> int:
        length = len(numbers)
        count = defaultdict(int)
        total = 0
        pairs = 0
        left = 0

        for right, num in enumerate(numbers):
            pairs += count[num]
            count[num] += 1
            while pairs >= min_pairs:
                total += length - right
                count[numbers[left]] -= 1
                pairs -= count[numbers[left]]
                left += 1

        return total