class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        if l > len(s):
            return []
        ans = []
        cp = {}
        left = 0
        right = 0
        sp = {}
        for ch in p:
            if ch in sp:
                sp[ch] += 1
            else:
                sp[ch] = 1
        

        
        while right < len(p):
            if s[right] in cp:
                cp[s[right]] += 1
            else:
                cp[s[right]] = 1
            right += 1
        
        if sp == cp:
            ans.append(left)
        
        while right < len(s):
            cp[s[left]] -= 1
            if cp[s[left]] == 0:
                del cp[s[left]]
            if s[right] in cp:
                cp[s[right]] += 1
            else:
                cp[s[right]] = 1
            
            if sp == cp:
                ans.append(left + 1)
            
            left += 1
            right += 1
        
        return ans