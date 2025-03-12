class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for val in s:
            if val == "(":
                stack.append(0)
            else:
                count = stack.pop()
                if count == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += count * 2

        return stack[-1]
            