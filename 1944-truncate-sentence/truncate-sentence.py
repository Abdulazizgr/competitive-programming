class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split(" ")
        ans = ""
        for i in range(k-1):
            ans = ans + a[i] + " "

        return ans + a[k-1]