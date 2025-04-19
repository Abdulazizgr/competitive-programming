class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        ans = 0    
        for row in grid:
            low = 0
            high = cols - 1
            
            if row[low] < 0:
                ans += cols
            else:
                while low <= high:
                    mid = (low + high) // 2
                    if row[mid] < 0:
                        high = mid - 1
                    else:
                        low = mid + 1
                
                ans += cols - low
        
        return ans