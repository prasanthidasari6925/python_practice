#lists(store digits in a list)
num=int(input())
num=abs(num)
digits=[]
while num>0:
    digits.append(num%10)
    num//=10
digits.reverse()
print(digits)
