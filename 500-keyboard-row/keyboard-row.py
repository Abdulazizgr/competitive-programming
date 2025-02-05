class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiopQWERTYUIOP")
        second_row = set("asdfghjklASDFGHJKL")
        third_row = set("zxcvbnmZXCVBNM")
        ans = []
        for value in words:
            count ,count1, count2 = 0,0,0
            for val in value:
                if val in first_row:
                    count += 1
                elif val in second_row:
                    count1 += 1
                else:
                    count2 += 1
            if count == len(value) or count1 == len(value) or count2 == len(value):
                ans.append(value)
        return ans
                
        

