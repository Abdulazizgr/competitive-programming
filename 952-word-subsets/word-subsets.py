class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_dict = defaultdict(int)
        for word in words2:
            fre_word = Counter(word)
            for key in word:
                word2_dict[key] = max(word2_dict[key],fre_word[key])

        ans = []
        for word in words1:
            flag = True
            word1_dict = Counter(word)
            for key,value in word2_dict.items():
                if value > word1_dict[key]:
                    flag = False
                    break

            if flag:
                ans.append(word)
         
        return ans
