class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            name = s.split("@")
            print(name)
            return name[0][:1] +"*****"+ name[0][-1:] +"@"+ name[1]
        else:
            nums =[]
            for i in range(len(s)):
                if s[i].isdigit():
                    nums.append(s[i])
            if len(nums) == 10:
                return "***-***-" + "".join(nums[-4:])
            elif len(nums) == 11:
                return "+*-***-***-" + "".join(nums[-4:])
            elif len(nums) == 12:
                return "+**-***-***-" + "".join(nums[-4:])
            elif len(nums) == 13:
                return "+***-***-***-" + "".join(nums[-4:])



                

