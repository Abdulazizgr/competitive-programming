class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}
        an=[]
        an1=[]
        for i in range(len(matches)):
            if matches[i][0] in winner:
                winner[matches[i][0]] += 1
            else:
                winner[matches[i][0]] = 1
        for i in range(len(matches)):
            if matches[i][1] in loser:
                loser[matches[i][1]] += 1
            else:
                loser[matches[i][1]] = 1
        for key in winner:
            if key not in loser:
                an.append(key)
        for key, value in loser.items():
            if value == 1:
                an1.append(key)
        an.sort()
        an1.sort()
        return [an,an1]