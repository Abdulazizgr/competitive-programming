class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # sorted_arr = sorted(arr)
        ans = []
        idx = len(arr) - 1
        
        while True:
            if idx > 0:
                max_num = max(arr[:idx+1])
                temp_idx = arr.index(max_num)
                
                arr[:temp_idx+1] = reversed(arr[:temp_idx+1])
                ans.append(temp_idx + 1)
                
                arr[:idx+1] = reversed(arr[:idx+1])
                ans.append(idx + 1)
                
                idx -= 1
            else:
                break
            

        return ans
