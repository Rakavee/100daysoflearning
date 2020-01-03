def atoi(input_string):
    if len(input_string) == 0:
        return 0
    
    min_int = -2147483648
    max_int = 2147483647

    input_string = input_string.strip()
    sign = ""
    if input_string[0] == "-":
        sign = "-"
        input_string = input_string[1:len(input_string)]
    elif input_string[0] == "+":
        input_string = input_string[1:len(input_string)]
    if not input_string or not input_string[0] in '1234567890':
        return 0
    output = ""
    #print(input_string)
    for each in input_string:
        #print(each)
        if each in '1234567890':
            output += each
            #print(output)
            continue
        break
    #print(output)
    output = int(output.strip())
    if sign == "-":
        output += -(2*output)
    output = max(output, min_int)
    output = min(output, max_int)
        
    return output

print(atoi("-3456789876543234567898765432"))
print(atoi("-34567"))
print(atoi("3456"))
print(atoi("3456789876543234567898765432"))
print(atoi(" 3456789"))
print(atoi("34567jf8987gdfhbsjsk6543234567898765432"))
print(atoi("-345  6789j "))  
print(atoi("gh3456789 "))   
print(atoi(" 3456789  "))
print(atoi(" hj3456789"))
print(atoi(" ++3456789"))


#Reference: https://leetcode.com/problems/string-to-integer-atoi/