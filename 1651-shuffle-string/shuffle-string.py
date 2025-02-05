class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst =[]
        ans = ""
        for i in range(len(s)):
            lst.append((indices[i],s[i]))
        lst.sort()
        for val in lst:
            ans += val[1]
        return ans


    