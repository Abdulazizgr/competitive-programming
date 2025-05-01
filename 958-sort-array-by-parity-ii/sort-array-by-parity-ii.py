class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        res = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for idx in range(len(nums)//2):
            res.append(even[idx])
            res.append(odd[idx])
        return res
