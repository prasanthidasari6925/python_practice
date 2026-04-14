#Armstrong Number
num=int(input())
temp=num
sum_digit=0
while num>0:
    last_digit=num%10
    sum_digit=sum_digit+last_digit**3
    num=num//10
if temp==sum_digit:
    print(f"{temp} is an armstrong number")