class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        _sum = 0

        for idx in range(len(costs)//2):
            _sum += costs[idx][0]
        for idx in range(len(costs)//2,len(costs)):
            _sum += costs[idx][1]
        return _sum

        
        
