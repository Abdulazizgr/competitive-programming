class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0] * (len(nums) +1)

        for start ,end in requests:
            pre[start] += 1
            pre[end + 1] -= 1
        pre = list(accumulate(pre))
        pre.sort(reverse=True)
        nums.sort(reverse=True)

        _sum = sum(nums[i] * pre[i] for i in range(len(nums)))

        return _sum % (10**9 + 7)



      

        return 