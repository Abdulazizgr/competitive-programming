class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        seen = set()
        steps = 0
        for val in s:
            if val in cnt_t:
                if cnt_s[val] > cnt_t[val] and val not in seen:
                    steps += cnt_s[val] - cnt_t[val]
                    seen.add(val)

                    print(steps,"HI")
            elif val not in seen:
                steps += cnt_s[val]
                seen.add(val)
        return steps

        