class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        cnt = Counter(nums)
        ans = []

        for key,value in cnt.items():
            if value > n :
                ans.append(key)
        return ans
