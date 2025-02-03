class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win =defaultdict(int)
        los = defaultdict(int)
        ans1 =[]
        ans0= []
        for i in range(len(matches)):
            win[matches[i][0]] += 1
            los[matches[i][1]] += 1
        for i in win:
            if i not in los:
                ans0.append(i)
        for k,v in los.items():
            if v == 1:
                ans1.append(k)
        ans1.sort()
        ans0.sort()
        return [ans0,ans1]
        