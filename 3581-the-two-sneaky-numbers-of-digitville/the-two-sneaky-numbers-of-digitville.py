class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num = Counter(nums)
        ans =[]

        for key ,value in num.items():
            if value == 2:
                ans.append(key)


        return ans
        