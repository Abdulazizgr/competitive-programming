class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pep = list(zip(names,heights))
    
        n = len(pep)
  

        for i in range(n):
            for j in range(n - i - 1):
                if pep[j][1] < pep[j + 1][1]:  
                    pep[j], pep[j + 1] = pep[j + 1], pep[j]
        
 
        return [name for name, _ in pep]


