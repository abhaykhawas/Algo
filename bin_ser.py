x_list = [5,3,8,11,23,89,75,0]

x_list.sort()

x = 75

min_index = 0

max_index = len(x_list)-1

while True:
    if min_index > max_index:
        print("No solution")
        break

    mid_index = (min_index + max_index) // 2

    if x_list[mid_index] == x:
        print("Number was found")
        break

    elif x > x_list[mid_index]:
        min_index = mid_index + 1

    elif x < x_list[mid_index]:
        max_index = mid_index - 1
    
