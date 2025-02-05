class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res =[]
        for val in words:
            char = Counter(chars)
            count = 0
            for i in val:
                if i in char:
                    count += 1
                    char[i] -= 1
                    if char[i] == 0:
                        del char[i]
                else:
                    break 
            if count == len(val):
                res.append(count)

        return sum(res)