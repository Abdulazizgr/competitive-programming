class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        ans = 0
        i = 0
        for j in range(n):
            if nums[j] % 2 == 1:
                count += 1
                print (count)
            while count > k:
                if nums[i] % 2 == 1:
                    count -= 1
                i += 1
            p = i
            count1 = count
            while count1 == k:
                ans += 1
                if nums[p] % 2 == 1:
                    count1 -= 1
                p += 1
        return ans


            

