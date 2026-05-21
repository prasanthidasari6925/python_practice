#difference between minimum and maximum
num=list(map(int,input().split()))
max_element=num[0]
min_element=num[0]
diff_of_minmax=0
for i in range(1,len(num)):
    if num[i]>max_element:
        max_element=num[i]
    elif num[i]<min_element:
        min_element=num[i]
diff_of_minmax=max_element-min_element
print(diff_of_minmax)