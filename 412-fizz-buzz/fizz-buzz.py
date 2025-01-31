class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        y=[]
        i = 1
        while i <= n :
            z=i%3
            a=i%5
            if(z==0 and a==0):
                y.append( "FizzBuzz")
            elif(z==0):
                y.append("Fizz")
            elif(a==0):
                y.append("Buzz")
            else:
                b=str(i)
                y.append(b)
            i += 1
        return(y)