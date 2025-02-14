class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_s = Counter()
        left = 0
        current_min = float('inf')
        ans = ""
        for right in range(len(s)):
            freq_s[s[right]] += 1

            while freq_t <= freq_s:
                if current_min > right - left + 1 :
                    current_min = right - left + 1
                    ans = s[left:right+1]
                freq_s[s[left]] -= 1
                if freq_s[s[left]] == 0:
                    del freq_s[s[left]]
                left += 1
            

            
        return ans 
