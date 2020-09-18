def recursion_function(n):
     if(n==1):
      return n
     elif(n>1):
         return n*recursion_function(n-1)
     elif(n==0):
         print("the factorial of 0 is 1:")
     else:
         
       print("factorial is not defined:")
