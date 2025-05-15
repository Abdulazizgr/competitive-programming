class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)

        for idx in range(0,len(lst),2*k):
            lst[idx:idx+k] = reversed(lst[idx:idx+k])
        
        return "".join(lst) 
