#Strong number
num=int(input())
num=abs(num)
temp=num
sum_of_factorials=0
while num>0:
    digit=num%10
    if digit==0:
        factorial=1
        sum_of_factorials+=factorial
    else:
        factorial=1
        for i in range(1,digit+1):
            factorial*=i
        sum_of_factorials+=factorial
    num=num//10
if sum_of_factorials==temp:
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")