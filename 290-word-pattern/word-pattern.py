class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        p = list(pattern)
        print(s,p)
        dic = {}
        dics ={}

        if len(s) == len(p):
            for i in range(len(p)):
                if p[i] in dic:
                    if dic[p[i]] != s[i]:
                        return False
                else:
                    dic[p[i]] = s[i]
            for i in range(len(p)):
                if s[i] in dics:
                    if dics[s[i]] != p[i]:
                        return False
                else:
                    dics[s[i]] = p[i]
        else:
            return False
        return True
                    
               
        print(dic)
       
      
        # return (len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern,s))))