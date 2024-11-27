class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen =  defaultdict(int)
        left = 0
        right = 0
       
        ans =0
        while right < len(s):
            if seen[s[right]] == 1:
                ans = max(ans,len(seen))
                while seen[s[right]] == 1:
                    seen[s[left]] -=1
                    if seen[s[left]] == 0:
                        del seen[s[left]]
                        left +=1
            seen[s[right]] += 1
            right +=1
        ans = max(ans,len(seen))
        
        print(ans)
        return ans




        