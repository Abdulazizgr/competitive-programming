class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        ask = [] 
        for i in range (len(s)):
            ask.append(ord(s[i]))
            score += abs(ask[i]-ask[i-1])
        return score