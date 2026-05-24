#rotate list right by one
num=list(map(int,input().split()))
temp=num[-1]
for i in range(len(num)-1,-1,-1):
    num[i]=num[i-1]
num[0]=temp
print(num)