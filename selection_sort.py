x_list = [5,3,8,11,23,89,75,0]




for i in range(len(x_list)-1):
    min_index = i

    for j in range(i+1, len(x_list)):
        if x_list[j] < x_list[min_index]:
            min_index = j



    x_list[i], x_list[min_index] = x_list[min_index] , x_list[i]
    
print(x_list)
