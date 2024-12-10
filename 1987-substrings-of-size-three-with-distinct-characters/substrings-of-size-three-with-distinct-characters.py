class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        ans = 0
       

        for i in range(len(s)-2):
            win = s[i:i+3]

            if len(set(win)) == len(win):
                ans += 1 
        return ans

