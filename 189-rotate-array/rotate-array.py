class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        def reverse(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        reverse(0,k-1)
        reverse(k,len(nums)-1)
        



        # k= k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]