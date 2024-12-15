class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        r = len(boxGrid)
        c = len(boxGrid[0])
        ans = []

        for ro in range(r):
            i = c -1
            for co in reversed(range(c)):
                if boxGrid[ro][co] == "#":
                    boxGrid[ro][co] ,boxGrid[ro][i] = boxGrid[ro][i],boxGrid[ro][co] 
                    i -=   1 


                elif boxGrid[ro][co] == "*":
                    i = co - 1
        # print(new_mat)
        for j in range(c):
            col = []
            for i in reversed(range(r)):
                col.append(boxGrid[i][j])
            ans.append(col)
        



        return ans