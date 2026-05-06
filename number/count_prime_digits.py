#count prime digits
num=int(input())
num=abs(num)
count=0
while num>0:
    digit=num%10
    if digit in (2,3,5,7):
        count+=1
    num//=10
print(count)