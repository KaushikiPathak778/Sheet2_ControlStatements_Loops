# You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A.
n=int(input("Enter a positive integer: "))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print("Sum of the even numbers=",sum)
