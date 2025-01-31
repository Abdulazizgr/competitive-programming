class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            a = str(nums[i])
            if len(a) != 1:
                for j in range(len(a)):
                    ans.append(int(a[j]))
            else:
                ans.append(nums[i])

                
     
        
        return ans