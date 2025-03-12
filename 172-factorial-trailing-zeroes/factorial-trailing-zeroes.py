class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num <= 1:
                return 1
    
            return num * factorial(num - 1)
        if n == 0:
            return 0
        num = factorial(n)
        count = 0
        while num % 10 == 0:
            num = num // 10
            count += 1
        return count

