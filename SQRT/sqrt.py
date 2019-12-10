def squareRoot(number, precision): 
  
    start = 0
    end = number 
    while start <= end: 
        mid = (start + end) // 2 
        if mid * mid == number: 
            output = mid 
            break
        if mid * mid < number: 
            start = mid + 1
            output = mid 
        else: 
            end = mid - 1

    increment = 0.1
    for i in range(precision):  
        while output * output < number: 
            output += increment 
        increment = increment / 10
      
    return output
  
print("Squareroot of 10 with percision 3: ",squareRoot(10, 3)) 
print("Squareroot of 25 with percision 4: ",squareRoot(25, 4)) 
print("Squareroot of 31 with percision 2: ",squareRoot(31, 2))