class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        freq = defaultdict(int)
        max_length = 0


        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            max_length = max(max_length,right - left + 1)

        return max_length


