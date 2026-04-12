#largest digit in a num
num=int(input())
num=abs(num)
max_digit=0
while num>0:
    last_digit=num%10
    if last_digit>max_digit:
        max_digit=last_digit
    num=num//10
print(max_digit)