class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set1 = set()
        for i in range(left,right + 1):
            set1.add(i)
        set1 = list(set1)
        count = 0
        flag = 0

        print(set1)
        for i in range(len(set1)):
            for j in range(len(ranges)):
                if set1[i] >= ranges[j][0] and set1[i] <= ranges[j][1]:
                    count += 1
                    flag =1
                    break
            if flag == 0:
                count -= 1
            print(count)
        if count < len(set1):
            return False
        return True


    