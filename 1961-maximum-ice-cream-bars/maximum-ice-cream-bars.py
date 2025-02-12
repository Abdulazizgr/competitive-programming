class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        count = 0
        price_sum = 0
        for price in costs:
            if price > coins:
                break
            else:
                price_sum += price
                if price_sum <= coins:
                    count += 1
                else:
                    break
        return count

