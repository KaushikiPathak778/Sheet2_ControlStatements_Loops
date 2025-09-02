# Read N, Print no. of digits in N.
N=int(input("Enter the number:"))
count=0
num = abs(N)  
if num == 0:
    count = 1  
else:
    while num > 0:
        num //= 10   
        count = count+1   
print("Number of digits in N is:",count)