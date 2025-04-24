class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res = 0
        pre_sum = 0

        for num in satisfaction:
            pre_sum += num
            if pre_sum < 0:
                return res
            else:
                res += pre_sum
        return res
        
        

        return res