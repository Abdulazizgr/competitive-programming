class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            base_n = []
            num = n  
            while num > 0:
                base_n.append(num % i)
                num = num // i
            # print(base_n)
            
            if base_n != base_n[::-1]:
                return False
        return True