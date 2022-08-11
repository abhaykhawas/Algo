x_list = [5,3,8,11,23,89,75,0]


for i in range(len(x_list) - 1):
    
    for j in range (len(x_list) - i - 1):

        if x_list[j] > x_list[j+1]:
            x_list[j], x_list[j+1] = x_list[j+1], x_list[j]



print(x_list)
