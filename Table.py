# Take a number A as input, print its multiplication table having the first 10 multiples.
num=int(input("Enter the number:\n"))
print("MULTIPLICATION TABLE OF:",num)
for i in range(1,11):
    print(num,"x",i,"=",num*i)