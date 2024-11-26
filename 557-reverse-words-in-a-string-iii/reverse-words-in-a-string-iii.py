class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        ans=[]
        # print(len(s))
        while right < len(s):
            if s[right] == " ":
                a = s[left:right ][::-1]
                print(a)
                ans.append(a)
                left = right + 1
            right += 1
            # print(left)
        ans.append(s[left:right ][::-1])
        # print(ans)
        res = ' '.join(ans)
    
        return res 
            

