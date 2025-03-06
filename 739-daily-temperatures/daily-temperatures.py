class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = 0
        ans = [0] * len(temperatures)
        stack = []
        for temp in temperatures:
            while stack and stack[-1][0] < temp:
                val = stack.pop()
                res = index - val[1] + 1
                ans[val[1]-1] = res
            stack.append([temp,index+1])
            index += 1
        return ans
        