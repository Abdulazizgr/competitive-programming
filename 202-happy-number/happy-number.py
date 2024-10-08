class Solution:
    def isHappy(self, n: int) -> bool:
        lis = []
        while n not in lis:
            lis.append(n)
            a = list(str(n))
            b=0
            for i in a:
                b += int(i)**2
                print(b)
            n = b
                

            if n == 1:
                return True
        return False


            