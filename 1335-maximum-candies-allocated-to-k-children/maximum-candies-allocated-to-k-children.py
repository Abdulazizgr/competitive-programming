class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def isValid(mid):
            count = 0
            for candy in candies:
                if mid > 0:
                    count += (candy // mid)
            return count >= k

        candies.sort()
        low = 1
        high = candies[-1]
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                print("te")
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
