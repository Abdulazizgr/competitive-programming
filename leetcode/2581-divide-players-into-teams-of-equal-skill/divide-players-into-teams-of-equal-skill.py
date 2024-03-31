class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        sum = skill[0] + skill[-1]
        an = 0
        start = 0
        end = n -1
        if n == 2:
            return skill[0] * skill[1]
        while (start < end):
            if skill[start] + skill[end] != sum:
                return -1
            else:
                an += skill[start] * skill[end]
                start += 1
                end -= 1
        return an
                
