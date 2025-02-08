from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)] 
        def isvalid(r,c):
            return 0 <= r < len(img) and 0 <= c < len(img[0]) 
        for row in range(rows):
            for col in range(cols):
                surrounding = [
                    [row-1,col],[row+1,col],[row,col-1],
                    [row,col+1],[row-1,col-1],[row+1,col+1],
                    [row-1,col+1],[row+1,col-1]
                ]
                count = 1
                sum_n = img[row][col]
                for r,c in surrounding:
                    if isvalid(r,c):
                        count += 1
                        sum_n += img[r][c]

                result[row][col] = sum_n // count  
        return result  