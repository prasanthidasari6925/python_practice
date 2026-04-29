#LCM
num1=int(input())
num2=int(input())
num1=abs(num1)
num2=abs(num2)
LCD=0
while num1>0 and num2>0:
    for i in range(1,(num1*num2)+1):
        if i%num1==0 and i%num2==0:
            LCD=i
            break
    print(LCD)