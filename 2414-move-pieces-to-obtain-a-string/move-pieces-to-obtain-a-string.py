class Solution:
    def canChange(self, start: str, target: str) -> bool:

        if start.count('L') != target.count('L') or start.count('R') != target.count('R'):
            return False


            
        n = len(start)
        i = j = 0
        
        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            if i == n and j == n:
                break
            
            if (i == n) != (j == n) or start[i] != target[j]:
                return False
            
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            
            i += 1
            j += 1
        
        return True






        # left = 0
        # start = list(start)
        # n = len(start)
        # # print(start)
        # for right in range(1,n):
        #     if start[left] == '_' and start[right] == 'L':
        #         start[left],start[right] = start[right],start[left] 
        #         while left -1 > 0 and start[left-1] =='_':
        #             if start[left-1] == '_' and start[left] == 'L':
        #                 start[left-1],start[left] = start[left],start[left-1] 
        #             left -= 1
        #         left = right 
            
                
        #     elif start[left] == 'R' and start[right] == '_':
        #         start[left],start[right] = start[right],start[left] 
        #         while left -1 > 0 and start[left-1] =='R':
        #             if start[left-1] == 'R' and start[left] == '_':
        #                 start[left-1],start[left] = start[left],start[left-1] 
        #             left -= 1
        #         left = right 
        #     # print(start)
        #     left += 1
            
        # return ''.join(start) == target

