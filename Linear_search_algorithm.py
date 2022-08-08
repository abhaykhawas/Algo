numbers = [55,32,65,12,0,20]
x = 12
flag = 0
for i in range(len(numbers)):
    if x == numbers[i]:
        print(i)
        flag = 1
        break
if flag == 0:
    print("Number not found")
