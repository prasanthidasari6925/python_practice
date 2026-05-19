#average of elements in a list
num=list(map(int,input().split()))
sum_of_elements=0
for i in range(0,len(num)):
    sum_of_elements+=num[i]
avg_elements=sum_of_elements/len(num)
print(avg_elements)
