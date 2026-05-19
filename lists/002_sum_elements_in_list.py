#sum of the elements in a list.
num=int(input())
num=abs(num)
digits=[]
while num>0:
    digits.append(num%10)
    num//=10
digits.reverse()
sum_of_digits=digits[0]
for i in range(1,len(digits)):
    sum_of_digits+=digits[i]
print(sum_of_digits)
