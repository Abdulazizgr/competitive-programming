if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    allEle = [[i, j, k] for i in range(x+1) for j in range(y+1)for k in range(z+1)]
    an = [ele for ele in allEle if sum(ele) != n]
    
    print(an)
