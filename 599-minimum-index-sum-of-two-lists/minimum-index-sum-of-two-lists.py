class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = len(list1) + len(list2)
        ans = []
        res =[]
        for val in range(len(list1 )):
            if list1[val] in list2:
                index = list2.index(list1[val])
                print(min_index,index+val,index)
                if index + val < min_index or index + val == min_index:
                    ans.append((index + val,val))
                    min_index = val + index
        ans.sort()
        min_index = ans[0][0]
        for i in ans :
            if i[0] == min_index:
                res.append(list1[i[1]])

      
        return res
                    
            
            