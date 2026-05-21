#Creating a new list containing only even digits
num=list(map(int,input().split()))
even_digits=[]
for i in range(0,len(num)):
    if num[i]%2==0:
        even_digits.append(num[i])
print(even_digits)