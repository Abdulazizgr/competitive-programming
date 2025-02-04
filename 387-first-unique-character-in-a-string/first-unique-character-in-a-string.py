class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for val in range(len(s)):
            if s[val] in cnt:
                if cnt[s[val]] == 1:
                    return val
        return -1

   