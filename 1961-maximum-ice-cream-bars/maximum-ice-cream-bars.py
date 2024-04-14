class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins < costs[0]:
            return 0
        sum = 0
        count =0
        print(costs)
        for i in range(len(costs)):
            sum += costs[i]
            if sum <= coins:
               
                count += 1
                print(sum)
            else:
                break
        return count