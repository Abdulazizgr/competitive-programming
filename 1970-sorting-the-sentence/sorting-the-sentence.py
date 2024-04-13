class Solution:
    def sortSentence(self, s: str) -> str:
       lis = []
       j=0
       for i in range(len(s)):
        if s[i] == " ":
            lis.append(s[j:i])
            j = i + 1
       lis.append(s[j:len(s)])
       sorted_list = sorted(lis, key=lambda x: x[-1])
       print(sorted_list)
       strr = ""
       for i in sorted_list:
        ans = i[:-1]
        strr = strr + " " + ans
       return strr[1:]
