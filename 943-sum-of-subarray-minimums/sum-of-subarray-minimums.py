class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        mod = 10**9 + 7

        for idx in range(len(arr)):
            while stack and arr[idx] < stack[-1][0]:
                val, index = stack.pop()
                left = index - stack[-1][1] if stack else index + 1
                right = idx - index
                ans = (ans + val * left * right) % mod  
            stack.append((arr[idx], idx))

       
        while stack:
            val, index = stack.pop()
            left = index - stack[-1][1] if stack else index + 1
            right = len(arr) - index
            ans = (ans + val * left * right) % mod  

        return ans
