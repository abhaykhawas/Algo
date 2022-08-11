x_list = [5,3,8,11,23,89,75,0]



for i in range(1, len(x_list)):
    key = x_list[i]

    j = i - 1
    while j>=0 and key < x_list[j]:
        x_list[j+1] = x_list[j]
        j-=1
        x_list[j+1] = key
    x_list[j+1] = key


print(x_list)
