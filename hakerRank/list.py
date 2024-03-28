if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        line = input().split()
        command = line[0]
        args = list(map(int, line[1:]))
        
        if command == "insert":
            index = args[0]
            element = args[1]
            result.insert(index, element)
        elif command == "print":
            print(result)
        elif command == "remove":
            element = args[0]
            result.remove(element)
        elif command == "append":
            element = args[0]
            result.append(element)
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result.reverse()
