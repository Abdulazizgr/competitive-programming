class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
       
        stack = []
        num1 = float('-inf')
        nums.reverse()
        for num in nums:
            if num < num1:
                return True

            while stack and stack[-1] < num:
                num1 = stack.pop()

            stack.append(num)

        return False
