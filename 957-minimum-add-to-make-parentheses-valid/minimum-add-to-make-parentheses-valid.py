class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s = list(s)
        ope =0 
        clo = 0
        for i in range(len(s)):
            if s[i] == "(":
                ope += 1
            else:
                if ope > 0:
                    ope -=1
                else:
                    clo += 1
        return ope + clo
      



        