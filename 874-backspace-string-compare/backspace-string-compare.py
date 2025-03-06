class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        for val in s:
            if stackS and  val == "#":
                stackS.pop()
            elif val != "#":
                stackS.append(val)
        stackT = []
        for val in t:
            if stackT and val == "#":
                stackT.pop()
            elif val != "#":
                stackT.append(val)
        print(stackS,stackT)
        return stackS == stackT