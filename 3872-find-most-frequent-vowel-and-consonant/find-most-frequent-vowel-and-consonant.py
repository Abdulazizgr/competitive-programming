class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowel = 0
        consonant = 0
        for key,value in count.items():
            if key in 'aeiou':
                vowel = max(vowel,count[key])
            else:
                consonant = max(consonant,count[key])
        return consonant + vowel
