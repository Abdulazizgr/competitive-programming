class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        le = 0
        ri = 0

        while le <= len(name) and ri < len(typed):
            if le < len(name) and typed[ri] == name[le] :
                le += 1
                ri += 1
            elif typed[ri] == name[le-1] and le != 0:
                ri += 1
            else:
                return False
            
        return le == len(name) and ri == len(typed)

        