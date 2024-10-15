class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n = len(score)
        dic = {}
        for i in range(n):
            dic[score[i][k]] = score[i]
        ans = dict (sorted(dic.items(),reverse=True))
        value = list(ans.values())
        
        
       



        return value