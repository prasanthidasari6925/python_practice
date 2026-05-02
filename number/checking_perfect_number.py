#checking perfect number
num=int(input())
if num<=1:
    print{"not perfect number"}
else:
sum_of_divisors=0
for i in range(1,(num//2)+1):
    if num%i==0:
        sum_of_divisors=sum_of_divisors+i
if sum_of_divisors==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")