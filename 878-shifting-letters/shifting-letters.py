class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [0] * (len(s) + 1)
        pref = [0] * (len(s))
        for i in range(len(s)):
            prefix[i+1] = prefix[i] + shifts[i]
        for i in range(1,len(prefix)):
            pref[i-1] = prefix[-1] - prefix[i-1]
        s = list(s)
        for idx in range(len(s)):
            s[idx] = chr((ord(s[idx]) - ord('a') + pref[idx]) % 26 + ord('a'))
        print(s)

        return "".join(s)