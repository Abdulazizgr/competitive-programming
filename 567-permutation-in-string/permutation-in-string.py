class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        n = len(s1)
        # print(Counter(s2[3:5]) == Counter(s1))
        print(Counter(s2[1:4]) == Counter(s1))

        for i in range(len(s2)-n+1):
            s2c = Counter(s2[i:i+n])
            print(s2c,len(s2)-n)
            if s1c == s2c:
                return True
        return False

      
      




        # l = 0
        # r  =0
        # count = 0

        # s1 = s1[::-1]
        # print(s1)

        # while l < len(s1) and r < len(s2):
        #     if s1[l] == s2[r]:
        #         print(s2[l:len(s1)],s1[:])
        #         if s1[:] == s2[l:len(s1)]:
        #             return True
             
                
        #         r += 1
        #     else:
        #         r += 1
      
       
        # return False


      