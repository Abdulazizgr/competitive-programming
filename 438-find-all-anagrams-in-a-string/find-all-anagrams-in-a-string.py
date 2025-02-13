class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        freq_p = Counter(p)
        freq_s = Counter(s[:len(p) - 1])  
        result = []
        
        left = 0
        for right in range(len(p) - 1, len(s)):
            freq_s[s[right]] += 1  
            
            if freq_s == freq_p:  
                result.append(left)
            
            freq_s[s[left]] -= 1  
            if freq_s[s[left]] == 0:
                del freq_s[s[left]]
            left += 1  
        
        return result
