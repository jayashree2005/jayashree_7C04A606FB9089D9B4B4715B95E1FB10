n=int(input("enter the number:"))
fact=1
count=2
if n==0:
  print("factorial of 0 is 1")
if n>0:
  while(count<=n):
    fact=fact*count
    count=count+1
print("the factorial of the given number:",fact)