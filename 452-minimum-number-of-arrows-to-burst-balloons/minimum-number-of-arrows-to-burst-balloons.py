class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        endPoint = points[0][1]
        count = 1

        for start,end in points:
            if start > endPoint:
                count += 1
                endPoint = end
               
        return count