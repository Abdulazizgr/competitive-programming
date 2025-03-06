class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        if path[-1] == '':
            path.pop()
        for val in path:
            if  val == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            elif val == '.':
                continue 
            elif val == '':
                continue 
            else:
                stack.append('/'+ val)
        
        if not stack:
            stack.append('/')
        return "".join(stack)