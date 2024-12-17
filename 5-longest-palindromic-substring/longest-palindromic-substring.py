class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        ans = 0
        sub = []
        for i in range(len(s)):
            st = i 
            end = i
            while st >= 0 and end < len(s) and s[st] == s[end]:
                if end - st + 1 > ans :
                    sub = s[st:end+1]
                    ans = end - st + 1
                st -= 1
                end += 1
               
        
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > ans:
                    sub = s[l:r+1]
                    ans = r -l  + 1
                l -= 1
                r += 1
                    
        return sub

                