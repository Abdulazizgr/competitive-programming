class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for val in answers:
            if val == 0:
                ans += 1  
            elif count[val] == 0: 
                count[val] = val  
                ans += val + 1  
            else:
                count[val] -= 1 
        return ans
