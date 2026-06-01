#Remove duplicate without using sets
num=list(map(int,input().split()))
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)