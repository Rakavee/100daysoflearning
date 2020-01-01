NO_OF_CHARS = 256
def longest_substring_without_repetition(input_string):
    current_length = 1
    max_length = 1
    previous_occurrence = 0
    i = 0
    end = 1
    visited_chars = [-1]*NO_OF_CHARS
    visited_chars[ord(input_string[0])] = 0 #first character's first occurrence

    for i in range(1,len(input_string)):
        previous_occurrence = visited_chars[ord(input_string[i])]
        if previous_occurrence == -1 or i - current_length > previous_occurrence:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                end = i
            current_length = i - previous_occurrence

        visited_chars[ord(input_string[i])] = i
    if current_length > max_length:
        max_length = current_length
        end = i
    start = end-max_length
    print(input_string[start:start+max_length])
    #print(max_length, end)

if __name__ == "__main__":
    input_string = "geeksforgeeks"
    longest_substring_without_repetition(input_string)