# You are given an integer A as input, and you need to determine whether it is a palindrome or not
n=int(input("Enter the number:\n"))
rev=0
a=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if(a==rev):
    print("Given number is palindrome\n")
else:
    print("Given number is not palindrome")