#GCD euclidean algorithm. optimized version.
num1 = int(input())
num2 = int(input())
num1 = abs(num1)
num2 = abs(num2)
while num2!=0:
    num1,num2=num2,num1%num2
print(num1)