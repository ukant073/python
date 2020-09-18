n = int(input("Enter the number:"))
sum = 0
temp = n
while temp>0:
 digit = temp%10
 sum +=  digit**3
 temp=temp//10
if(sum==n):
   print(n,"is a armstrong number")
else:
   print(n,"is not a armstrong number")     
cc