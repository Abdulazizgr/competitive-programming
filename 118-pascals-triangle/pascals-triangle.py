class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]  

        for i in range(1, numRows):  
            curr = [1]  
            for j in range(1, len(dp[-1])): 
                curr.append(dp[-1][j-1] + dp[-1][j])  
            curr.append(1) 
            dp.append(curr)  

        return dp
