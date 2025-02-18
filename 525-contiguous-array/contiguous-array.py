class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = -1
        max_length = -float('inf')
        for i in range(len(nums)) :
            count += 1 if nums[i] == 1 else -1
            
            if count not in prefix_count:
                prefix_count[count] = i
            else:
                max_length = max(max_length,i - prefix_count[count])
           
        return 0 if max_length == -float('inf') else max_length