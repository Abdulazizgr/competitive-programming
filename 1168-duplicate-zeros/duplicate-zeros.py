class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_lst = len(arr)
        new_lst = []
        for i in arr:
            if i == 0:
                new_lst.append(0)
            new_lst.append(i)


        arr.clear()
        arr.extend(new_lst[:len_lst])
            
        