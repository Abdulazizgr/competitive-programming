class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in blocks:
            if count == k :
                return 0
            elif i == "B":
                count += 1
            else:
                count = 0
        l = 0
        minop = blocks[:k].count("W")
        print(minop)
        print(len(blocks))
        for i in range(k,len(blocks)):
            coun = Counter(blocks[l:i])
            print(coun)
            l += 1
            minop = min(minop, coun["W"])
        minop = min(minop,Counter(blocks[l:len(blocks)+1])['W'])
        
        return minop
