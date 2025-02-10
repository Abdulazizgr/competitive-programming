class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        sorted_s = ""

        sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

        for char, freq in sorted_chars:
            sorted_s += char * freq

    
        return sorted_s
