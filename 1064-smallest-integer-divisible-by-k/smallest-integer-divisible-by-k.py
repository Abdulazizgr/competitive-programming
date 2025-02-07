class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        one_digit = 1
        length = 1
        for _ in range(k):
            if one_digit % k == 0:
                return length
            one_digit = (one_digit * 10 + 1) % k
            length += 1
        
        return -1
