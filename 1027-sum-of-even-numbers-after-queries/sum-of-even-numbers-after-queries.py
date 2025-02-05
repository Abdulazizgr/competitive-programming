class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        ans = sum([num for num in nums if num % 2 == 0])
        for value in queries:
            temp = nums[value[1]]
            nums[value[1]] += value[0]
            if nums[value[1]] % 2 == 0:
                ans += nums[value[1]]
            if temp % 2 == 0:
                ans -= temp
            res.append(ans)
            
        return res 