class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for value in strs:
            sorted_val = str(sorted(value))
            anagrams[sorted_val].append(value)
        return [val for val in anagrams.values()]
