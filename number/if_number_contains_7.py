#If number contains 7
num=int(input())
while num>0:
    a=num%10
    num=num//10
    if a==7:
        print('found')
        break
    elif a!=7:
        print('not found')
        break