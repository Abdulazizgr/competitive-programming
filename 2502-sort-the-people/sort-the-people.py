class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if heights[min_idx] < heights[j]:
                    min_idx = j
            heights[min_idx], heights[i] = heights[i], heights[min_idx]
            names[min_idx], names[i] = names[i], names[min_idx]
        return names
    
            



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
