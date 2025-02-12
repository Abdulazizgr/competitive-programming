class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) -1 
        sum_s = skill[left] + skill[right]
        total_sum = 0 
        while left < right :
            if sum_s == skill[left] + skill[right]:
                total_sum += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
    

        return total_sum
        


       
