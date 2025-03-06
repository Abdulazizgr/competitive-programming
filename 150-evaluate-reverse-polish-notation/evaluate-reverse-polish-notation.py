class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif val == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)  
            elif val == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif val == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))  
            else:
                stack.append(int(val))  

        return stack[-1]  
