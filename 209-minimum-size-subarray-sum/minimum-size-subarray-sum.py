class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = 0
        left = 0
        min_len = float('inf')

        for right in range(len(nums)):
            _sum += nums[right]

            while  _sum >= target:
                min_len = min(min_len ,right - left + 1)
                _sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0