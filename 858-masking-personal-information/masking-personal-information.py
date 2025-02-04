class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            name = s.split("@")
            print(name)
            return name[0][:1] +"*****"+ name[0][-1:] +"@"+ name[1]
        else:
            nums = ''
            for i in range(len(s)):
                if s[i].isdigit():
                    nums+= s[i]
            if len(nums) == 10:
                return "***-***-" + nums[-4:]
            else:
                return '+' + '*'* (len(nums)-10) + "-***-***-" + nums[-4:]


                

