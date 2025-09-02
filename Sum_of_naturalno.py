# Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user.
n=int(input("Enter a positive integer: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of the natural numbers=",sum)
