class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        # print(paragraph)
        word = words = re.findall(r'\b\w+\b', paragraph.lower())
        for i in range(len(word)):
            if "," in word[i] or "." in word[i] or "!" in word[i]:
                word[i] = word[i][:-1]
                # print(word[i])

        dic = Counter(word)
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        print(dic)
        for key,value in dic.items():
            if key not in banned:
                # print(key)
                return (str(key))
             


        


        