class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_block = False
        s = ""
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 1
                    else:
                        s += line[i]

                i += 1

            if s and not in_block:
                ans.append(s)
                s = ""

        return ans
