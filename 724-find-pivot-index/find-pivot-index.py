class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]* (len(nums) + 1)

        for i in range(1,len(nums) + 1):
            pre[i] = pre[i-1] + nums[i-1]
        # print(pre)
        for  val in range(1,len(pre)):
            if (pre[-1] - pre[val] ) == pre[val -1]:
                return val -1
        return -1 
