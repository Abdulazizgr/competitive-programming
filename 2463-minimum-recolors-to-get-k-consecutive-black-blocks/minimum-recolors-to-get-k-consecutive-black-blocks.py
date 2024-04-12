class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
     
        l = 0
        minop = blocks[:k].count("W")
        for i in range(k,len(blocks)):
            coun = Counter(blocks[l:i])
            
            l += 1
            minop = min(minop, coun["W"])
        minop = min(minop,Counter(blocks[l:len(blocks)+1])['W'])
        
        return minop
