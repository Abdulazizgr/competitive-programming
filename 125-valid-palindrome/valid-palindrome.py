class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in range(len(s)):
            if ord(s[i]) >= 97 and ord(s[i]) <= 122 or ord(s[i]) >= 48 and ord(s[i]) <= 57 :
                ans += s[i]
        print(ans)
    
        return ans == ans[::-1]