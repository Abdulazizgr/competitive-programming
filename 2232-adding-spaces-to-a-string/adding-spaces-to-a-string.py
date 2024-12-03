class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        l = 0
        i = 0
        for r in spaces:
            ans  = ans + s[l:r] +" "
            l = r
        return ans + s[r:]

