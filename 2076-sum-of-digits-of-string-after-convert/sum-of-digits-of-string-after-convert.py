class Solution:
    def getLucky(self, s: str, k: int) -> int:

        num = ""
        for i in s:
            num += str(ord(i.lower()) - ord('a') + 1)
     
         
        for _ in range(k):
            count = 0
            for i in num:
                count += int(i)
            num = str(count)
        return int(num)

            

