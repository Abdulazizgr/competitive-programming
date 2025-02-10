class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        ans = []
        map_pep = {}
        max_num = max(heights) +1
        freq = [0] *max_num
        for i in range(n):
            map_pep[heights[i]] = names[i]
        print(map_pep)
        for val in heights:
            freq[val] += 1
        for val in range(len(freq)-1 ,-1,-1):
            if freq[val] > 0:
                ans.append(map_pep[val])
        
                
     
        


        
        return ans







        # for i in range(n):
        #     idx = i
        #     for j in range(i - 1, -1, -1):
        #         if heights[j] < heights[idx]:
        #             heights[j], heights[idx] = heights[idx], heights[j]
        #             names[j], names[idx] = names[idx], names[j]
        #             idx = j
        #         else:
        #             break
        # return names







        # for i in range(n):
        #     min_idx = i
        #     for j in range(i+1,n):
        #         if heights[min_idx] < heights[j]:
        #             min_idx = j
        #     heights[min_idx], heights[i] = heights[i], heights[min_idx]
        #     names[min_idx], names[i] = names[i], names[min_idx]
        # return names
    
            



        # for i in range(n):
        #     for j in range(n -i -1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]
        # return names



        # values = []
        # for val in range(len(names)):
        #     values.append([names[val], heights[val]])
        # values.sort(key=lambda x: x[1], reverse=True)

        # return [name for name, height in values]
