class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0 
        n = set(allowed)
        
        for i in words:
            if set(i).issubset(n):
                count += 1
        return count

