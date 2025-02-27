class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

        ans = {}
        for word in words:
            s = ''
            for char in word:
                s += morse_dict[char]
            ans[s] = 1

        return len(ans)
