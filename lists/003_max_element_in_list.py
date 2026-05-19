#max value in a list
num=int(input())
num=abs(num)
digits=[]
while num>0:
    digits.append(num%10)
    num//=10
digits.reverse()
max_value=digits[0]
for i in range(1,len(digits)):
    if digits[i]>max_value:
        max_value=digits[i]
print(max_value)
