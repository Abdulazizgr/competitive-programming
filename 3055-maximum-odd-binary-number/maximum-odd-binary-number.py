class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        count_one = s.count('1')
        count_zero = s.count('0')
        ans = ['1'] * (count_one-1) + ['0'] * count_zero + ['1']
        
        return "".join(ans)