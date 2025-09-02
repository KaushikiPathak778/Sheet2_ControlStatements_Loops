# Take an integer A as input. You have to print the sum of all odd numbers in the range [1,A].
n=int(input("Enter a positive integer: "))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
print("Sum of the odd numbers=",sum)