class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        count = 1
        flag = True
        for i in range(time):
            if flag == True:
                count += 1
                if count == n:
                    flag = False
            else:
                count -= 1
                if count == 1:
                    flag = True
        return count

            




