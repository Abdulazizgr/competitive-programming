class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        conc = s + s
        if len(s) != len(goal):
            return False
        else:
            if goal in (conc):
                return True
            else:
                return False