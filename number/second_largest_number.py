#Second largest number
num = int(input())
num = abs(num)
digit = num % 10
largest = digit
sec_largest = -1
num = num // 10
while num > 0:
    digit = num % 10
    if digit > largest:
        sec_largest = largest
        largest = digit
    elif digit > sec_largest and digit != largest:
        sec_largest = digit
    num = num // 10
if sec_largest == -1:
    print("No second largest digit")
else:
    print(sec_largest)