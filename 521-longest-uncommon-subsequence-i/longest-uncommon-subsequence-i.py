class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a),len(b))
        # f ,s = 0,0
        # ans =0
        # count =0
        # print(len(a),len(b))
        # while f < len(a) and s < len(b):
        #     if a[f] != b[s]:
        #         count +=1
        #         f += 1
        #         s += 1
        #         ans = max(ans,count)
                
        #     else:
              
        #         count = 0
        #         f += 1
        #         s += 1
        # if ans == 0:
        #     return -1
        # else:
        #     return ans