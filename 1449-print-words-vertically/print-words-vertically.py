class Solution:
    def printVertically(self, s: str) -> List[str]:
        a = s.split(" ")
        s = s.split(" ")
        a.sort(key=len)
        n = len(a[-1])
        m = len(a)
        ans =[]
        for i in range(n):
            conc = ""
            for j in range(m):
                if i < len(s[j]):
                    conc += s[j][i]
                    print(conc)
                else:
                    conc += " "
            conc = conc.rstrip()
            ans.append(conc)




        return ans