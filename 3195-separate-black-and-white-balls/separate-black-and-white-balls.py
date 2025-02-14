class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        left = 0
        right = 1
        steps = 0
        
        while right < len(s):
            if s[left] == '1' and s[right] == '0':
                steps += right -left
                s[left], s[right] = s[right], s[left]
                left += 1
            
            right += 1
            
            if s[left] == '0': 
                left += 1

        return steps
