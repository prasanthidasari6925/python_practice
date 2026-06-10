#rotate list right by k times
num=list(map(int,input("Enter the list").split()))
k=int(input("How many times you want to rotate right:"))
k=k%len(num)
last_elements=num[-k:]
for i in range(len(num)-1,k-1,-1):
    num[i]=num[i-k]
num[:k]=last_elements
print(num)