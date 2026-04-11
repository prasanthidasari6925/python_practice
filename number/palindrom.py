#palindrome
num=int(input())
num=ab
s=0
temp=num
while num>0:
    s=s*10+num%10
    num=num//10
if s==temp:
    print(f"{temp} is palindrom")
else:
    print(f"{temp} is not a palindrome")