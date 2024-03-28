# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    x = int(input())
    an = map(int, input().split())
    t = tuple(an)
    print(hash(t))
