class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fi = 0
        te = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fi += 1
            elif bills[i] == 10 :
                fi -= 1
                te += 1
                if fi < 0:
                    return False
            else:
                if te > 0:
                    te -= 1
                    fi -= 1
                    if te < 0 or fi < 0:
                        return False
                else:
                    fi -= 3
                    if fi < 0:
                        return False
        return True

    
        

        print(fi)

        return True