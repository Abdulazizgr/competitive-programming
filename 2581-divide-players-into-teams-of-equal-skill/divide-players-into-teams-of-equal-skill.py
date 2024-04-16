class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        an = 0
        a = skill[0] + skill[-1]

        while left <= right:
            if skill[left] +skill[right] != a:
                return -1
            else:
                an += skill[left] * skill[right]
                left +=1
                right -=1
        return an