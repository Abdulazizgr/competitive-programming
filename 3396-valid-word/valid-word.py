class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False
        
        has_vowel = False
        has_consonant = False

        vowels = set("aeiouAEIOU")
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

        for char in word:
            if char not in valid_chars:
                return False
            if char in vowels:
                has_vowel = True
            elif char.isalpha():
                has_consonant = True

        return has_vowel and has_consonant
