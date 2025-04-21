class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int, list(str(num))))
        num.sort()
        new1 = int(str(num[0])+str(num[3]))
        new2 = int(str(num[1])+str(num[2]))

        return new1 + new2