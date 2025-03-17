class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char) 
            elif char == "[":
                stack.append((curr_str,num))
                curr_str = ""
                num = 0
            elif char == "]":
                ch , k = stack.pop()
                curr_str = ch + curr_str * k
            else:
                curr_str += char
        return curr_str


