class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = sorted(strs,key=len)
        b = len(a[0])
        c = a[0]
        count = 0 
        for i in range(b):
            for j in range(len(a)):
                print(c[i] ,a[j][i])
                if c[i] == a[j][i]:
                    count += 1
                else:
                    count = count // len(a)
                    return c[:count]
        count = count // len(a)
        return c[:count]

        
        