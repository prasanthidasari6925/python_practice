#Sum of proper divisors
num=int(input())
num=abs(num)
sum_div=0
for i in range(1,int(num/2)+1):
    if num%i==0:
        sum_div+=i
print(f"Sum of proper divisors:{sum_div}")