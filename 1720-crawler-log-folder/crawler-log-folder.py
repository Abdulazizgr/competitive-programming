class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for val in logs:
            if val == '../':
                if stack:
                    stack.pop()
            elif val != './':
                stack.append(val)
        return len(stack)