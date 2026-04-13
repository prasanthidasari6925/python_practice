#Count How Many Times a Digit Appears
num=int(input())
search_element=int(input())
count=0
while num>0:
    last_digit=num%10
    num=num//10
    if last_digit==search_element:
        count+=1
print(count)