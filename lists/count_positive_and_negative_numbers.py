#count positive and negative numbers
num=list(map(int,input().split()))
count_positive=0
count_negative=0
for i in range(0,len(num)):
    if num[i]>0:
        count_positive+=1
    elif num[i]<0:
        count_negative+=1
print(f"Number of positive numbers:{count_positive}")
print(f"Number of negative numbers:{count_negative}")