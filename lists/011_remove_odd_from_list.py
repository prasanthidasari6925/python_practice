#remove odd numbers from the list
num=list(map(int,input().split()))
for i in range(len(num)-1,-1,-1):
    if num[i]%2!=0:
        num.remove(num[i])
print(num)