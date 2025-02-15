from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        required = n // 4  
        char_count = Counter(s)  

        
        def is_balanced(counter):
            return all(counter[char] <= required for char in "QWER")

        
        if is_balanced(char_count):
            return 0
        # print(char_count,0)
        left = 0
        min_length = n  

        for right in range(n):
            char_count[s[right]] -= 1  
            # print(char_count)

            while is_balanced(char_count):  
                min_length = min(min_length, right - left + 1)
                char_count[s[left]] += 1  
                # print(char_count,1)
                left += 1  

        return min_length
