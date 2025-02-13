class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = dict()
        ans = []
        for idx in range(len(s)):
            index[s[idx]] =idx 
        start = 0
        end = 0
        last_end = 0

        while start < len(s):
            end = max(end,index[s[start]])
            if start == end:
                print(start,end)
                ans.append(end +1  - last_end )
                last_end = end +1
            start += 1

        return ans