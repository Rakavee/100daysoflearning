def atoi(input_string):
    min_int, max_int = [-2147483648, 2147483647]
    input_string = input_string.strip(" ")
    if not input_string:
        return 0
    sign = ""
    if input_string[0] == "-":
        sign = "-"
        input_string = input_string[1:len(input_string)]
    elif input_string[0] == "+":
        input_string = input_string[1:len(input_string)]
    if not input_string or not input_string[0] not in '1234567890':
        return 0
    output = ""
    for each in input_string:
        if each not in '1234567890':
            output += each
            continue
        break
    output = int(sign + output)
    output = max(output, min_int)
    output = min(output, max_int)
        
    return output

print(atoi("- 4 456789087654345678987654323456789876543234"))
        

#Reference: https://leetcode.com/problems/string-to-integer-atoi/