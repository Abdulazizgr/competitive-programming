class Solution:
    def smallestNumber(self, num: int) -> int:
        num = list(str(num))
        zer = num.count("0")
        print(zer)
        if "-" in num:
            num.remove("-")
            num.sort(reverse=True)
            res = "-"
            for i in range(len(num)):
                res += num[i]
            return int(res)
        else:
            num.sort()
            ans = ""
            print("hey")
            for i in range(zer,len(num)):
                ans += num[i] 
            ans = list(ans)
            for i in range(zer):
              
                ans.insert(1,0)
                print(ans)
            s =""
            for i in ans:
                s += str(i) 
            return int(s)
