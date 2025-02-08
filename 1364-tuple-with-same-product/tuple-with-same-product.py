class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        pairs = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pairs[nums[i]*nums[j]] += dic[nums[i]*nums[j]]
                dic[nums[i]*nums[j]] += 1
        
        count = 0
        for val in pairs.values():
            if val > 0:
                count += 8 *val


        return count
        