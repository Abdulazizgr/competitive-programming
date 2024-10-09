class Solution:
    def reverse(self, x: int) -> int:
      
        is_negative = x < 0
       
        x = str(abs(x))[::-1]
        
      
        x = int(x) if not is_negative else -int(x)
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0
