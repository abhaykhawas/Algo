#### Facorial
##def fact(n):
##    if n==1:
##        return 1
##    return n * fact(n-1)
##
##n = int(input("Number: "))
##print(fact(n))



#### Fibo series
##def recur_fibo(n):  
##   if n <= 1:  
##       return n  
##   else:  
##       return(recur_fibo(n-1) + recur_fibo(n-2))  
##
##n = int(input("Enter the number of terms: "))    
##if n <= 0:  
##   print("Plese enter a positive integer")  
##else:  
##   print("Fibonacci sequence:")  
##   for i in range(n):  
##       print(recur_fibo(i))  




#### nth number in fib series
##def Recursive_fib(n):
##  if n<0:
##    print("Incorrect input")
##  elif n==0:
##    return 0
##  elif n==1:
##    return 1
##  else:
##    return Recursive_fib(n-1) + Recursive_fib(n-2)
##
##print(Recursive_fib(5))





#### Question Problem 1
##def sumNum(n):
##    if n==0:
##        return 0
##    else:
##        return n%10 + sumNum(n//10)
##
##print(sumNum(12345))







#### Question Problem 2
##def reverse(val):
##    if len(val) == 1:
##        print(val, end="")
##    else:
##        a = val[0]
##        reverse(val[1:])
##        print(a, end="")
##
##
##reverse("Abhay")







#### Problem 3 Recursive Pascal's Triangle
##
##
##def pascals_triangle(n):
##    if n == 1:
##        return [[1]]
##    else:
##        result = pascals_triangle(n-1) 
##        current_row = [1]
##        previous_row = result[-1] 
##        for i in range(len(previous_row)-1):
##            current_row.append(previous_row[i] + previous_row[i+1])
##        current_row += [1]
##        result.append(current_row)
##        return result
##
##
##triangle = pascals_triangle(5)
##for row in triangle:
##    print(row)








