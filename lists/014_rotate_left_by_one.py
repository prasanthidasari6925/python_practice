#rotate list left by one
num=list(map(int,input().split()))
temp=num[0]
for i in range(len(num)-1):
    num[i]=num[i+1]
num[-1]=temp
print(num)