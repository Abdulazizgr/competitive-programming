class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]  

        for i in range(0, rowIndex):  
            curr = [1]  
            for j in range(1, len(dp[-1])): 
                curr.append(dp[-1][j-1] + dp[-1][j])  
            curr.append(1) 
            dp.append(curr)  
            

        return dp[-1]