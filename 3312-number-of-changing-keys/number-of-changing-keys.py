class Solution:
    def countKeyChanges(self, s: str) -> int:

        lst = [i.lower() for i in s]

        curr = 'ab'
        c = 0

        for i in lst:
            if i != curr:
                curr = i
                c += 1

        return c-1     