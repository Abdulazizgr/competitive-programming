#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # Create a copy of the input array
        lis = arr[:]
        lis.sort()
        
       
        return arr == lis

