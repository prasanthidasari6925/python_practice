#rotate list left by k times
num=list(map(int,input("Enter the list").split()))
k=int(input("How many times you want to rotate left:"))
k=k%len(num)
front_elements=num[:k]
for i in range(len(num)-k):
    num[i]=num[i+k]
num[-k:]=front_elements
print(num)