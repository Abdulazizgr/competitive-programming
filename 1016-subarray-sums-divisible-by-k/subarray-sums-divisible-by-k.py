class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        prefix_sum = list(accumulate(nums))
        for i in range(len(nums)):
            if prefix_sum[i] % k in prefix_count:
                count += prefix_count[prefix_sum[i] % k]
           
            prefix_count[prefix_sum[i] % k] += 1
    
        return count  