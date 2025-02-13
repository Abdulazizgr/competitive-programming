class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        if len(s1) > len(s2):
            return False
        freq_s1 = Counter(s1)
        freq_s2 = Counter(s2[:len(s1)-1])

        for right in range(len(s1)-1,len(s2)):
            freq_s2[s2[right]] += 1

            if freq_s1 == freq_s2:
                return True
            freq_s2[s2[left]] -= 1
            if freq_s2[s2[left]] == 0:
                del freq_s2[s2[left]]
            left += 1

        return False

