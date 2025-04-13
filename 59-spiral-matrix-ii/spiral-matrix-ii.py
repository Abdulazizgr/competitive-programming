class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        while bottom >= top and right >= left:
            # to the right 
            for col in range(left,right+1):
                ans[top][col] = num
                num += 1
            top += 1

            # to the bottom
            for row in range(top,bottom+1):
                ans[row][right] = num
                num += 1
            right -= 1

            # to the left
            if top <= bottom:
                for col in range(right,left-1,-1):
                    ans[bottom][col] = num
                    num += 1
                bottom -= 1
                
            # to the top
            if left <= right:
                for row in range(bottom,top-1,-1):
                    ans[row][left] = num
                    num += 1
                left += 1
            
        return ans 
         