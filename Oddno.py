# Write a program to print all odd numbers from 1 to N, where you have to take N as input from user.
n=int(input("Enter a positive integer: "))
for i in range(1,n+1,2):
    print(i,end=" ")
