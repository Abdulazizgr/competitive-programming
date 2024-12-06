class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        lst = []
        banned = set(banned)
        for i in range(1,n+1):
            if i not in banned:
                lst.append(i)
        sum = 0
        count = 0
        for i in lst:
            if sum + i <= maxSum:
                sum += i
                count += 1
            else:
                break

        print(lst)

        return count

