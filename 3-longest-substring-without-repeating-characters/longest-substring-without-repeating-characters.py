class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        curr = set()
        left = 0
        right = 0
        ans = 0
        
        while right < len(s):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            right += 1
            ans = max(ans, right - left)
        
        return ans