#LCM correct version
num1 = int(input())
num2 = int(input())
num1 = abs(num1)
num2 = abs(num2)
if num1 == 0 or num2 == 0:
    print(0)
else:
    i = max(num1, num2)
    while True:
        if i % num1 == 0 and i % num2 == 0:
            break
        i += max(num1, num2)
    print(i)