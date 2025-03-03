class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)

        for val in bills: 
            if val == 5:
                count [val] += 1
            elif val == 10:
                count[val] += 1
                if count[5] >= 1:
                    count[5] -= 1
                    if count[5] == 0:
                        del count[5]
                else:
                    return False
            else:
                if count[10] >= 1 and count[5] >= 1 :
                    count[10] -= 1
                    if count[10] == 0:
                        del count[10]
                    count[5] -= 1
                    if count[5] == 0:
                        del count[5]
                elif count[5] >= 3:
                     count[5] -= 3
                     if count[5] == 0:
                        del count[5]
                else:
                    return False
        return True




            
            