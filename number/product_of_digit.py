#product of digit
num=int(input())
product =1
while num>0:
    last_digit=num%10
    product=product*last_digit
    num=num//10
print(product)