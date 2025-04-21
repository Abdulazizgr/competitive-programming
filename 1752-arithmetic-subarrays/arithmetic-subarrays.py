class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for idx in range(len(l)):
            start = l[idx]
            end = r[idx] + 1
            temp = nums[start:end]
            temp.sort()
            ans = True
            if len(temp) > 1:
                diff = temp[1] - temp[0]
                for i in range(2,len(temp)):
                    if temp[i] - temp[i-1] != diff:
                        ans = False
                        break
            res.append(ans)
            
        return res