class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str =''
        for i in digits:
            num_str += "".join(str(i))
        num_str = str(int(num_str) + 1)
        ans = []
        for i in num_str:
            ans.append(int(i))

        return ans