#move all zeros to end
num=list(map(int,input("Enter sorted list 1:").split()))
result=[]
zero_count=0
for i in num:
    if i!=0:
        result.append(i)
    else:
        zero_count+=1
for i in range(zero_count):
    result.append(0)
print(result)