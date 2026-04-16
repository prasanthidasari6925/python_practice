#removing all zeros
num=int(input())
s=0
place=1
while num>0:
    last_digit=num%10
    if last_digit==0:
        s=s+last_digit
    else:
        s = s + (last_digit* place)
        place = place * 10
    num=num//10
print(s)