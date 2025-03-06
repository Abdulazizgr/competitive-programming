class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1 :
            if maxDoubles > 0 and target % 2 == 0:
                target = target // 2
                maxDoubles -= 1
                count += 1
            elif maxDoubles > 0 and target % 2 != 0:
                count += 1
                target -= 1
            else:
                target = target - 1
                count += target
                target = 1
        return count


