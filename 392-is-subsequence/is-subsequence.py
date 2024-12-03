class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # l = 0
        # count =0
        # for r in range(len(t)):
        #     if l < len(s) and s[l] == t[r]:
        #         count +=1
        #         l+=1
        # return count == len(s)
        f,se = 0,0
        count =0

        # if len(t) > 0 and len(s) > 0:
        while se < len(t) and f < len(s) :
            if s[f] == t[se]:
                count += 1
                f += 1
                se += 1
            else:
                se += 1
        if count == len(s):
            return True
        else:
            return False
        # elif  len(t) == 0 and len(s) > 0:
        #      return False
        # return True
