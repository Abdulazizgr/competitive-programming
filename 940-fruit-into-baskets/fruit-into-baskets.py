class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        left = 0
        max_sum = 0

        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_sum = max(max_sum ,right - left + 1)
        return max_sum