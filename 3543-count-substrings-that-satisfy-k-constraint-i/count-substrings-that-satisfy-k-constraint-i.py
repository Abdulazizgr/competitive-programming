class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        c0 = c1 = 0
        left = 0

        for r in range(len(s)):
            if s[r] == '1':
                c1 += 1
            else:
                c0 += 1
                # print(c0)
            while c1 > k and c0 > k:
                if s[left] == '1':
                    c1 -= 1
                else:
                    c0 -= 1
                left += 1
            ans += r -left + 1
        return ans
