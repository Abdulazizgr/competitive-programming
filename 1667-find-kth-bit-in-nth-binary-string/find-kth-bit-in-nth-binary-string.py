class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def generate(n):
            if n == 1:
                return "0"
            
            prev = generate(n - 1)
            inverted = ""
            for c in prev:
                if c == '0':
                    inverted += '1'
                else:
                    inverted += '0'
            return prev + "1" + inverted[::-1]

        return generate(n)[k - 1]
