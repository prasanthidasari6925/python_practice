#power of 2
num=int(input())
num=abs(num)
temp=num
if num<=0:
    print(f"{num} is not a power of 2")
while num%2==0:
    num=num//2
if num==1:
    print(f"{temp} is a power of 2")
else:
    print(f"{temp} is not a power of 2")