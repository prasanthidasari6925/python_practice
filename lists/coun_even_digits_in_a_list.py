#count even digits in a list
num=list(map(int,input().split()))
num=abs(num)
digits=[]
while num>0:
    digits.append(num%10)
    num//=10
digits.reverse()
count=0
for i in range(len(digits)):
    if digits[i]%2==0:
        count+=1
print(count)