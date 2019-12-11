
# coding: utf-8

# Given an input string, determine if the parentheses are matched and balanced. () [] {}

# In[17]:


#function to check if the parentheses are balanced.
def balanced_parentheses(string):
    open_list = ['(','{','['] #define the list of open parentheses.
    close_list = [')','}',']'] #define the list of close parentheses.
    stack = [] #stack data structure to match the open and close parentheses one by one maintaing the order.
    for i in string: #for each char in the string check for the matching parentheses.
        if i in open_list:
            stack.append(i) #push every open parentheses to the stack.
        elif i in close_list:
            if len(stack) > 0 and i == close_list[open_list.index(stack[-1])]: #check for the length of stack to match close parenthses.
                stack.pop() #pop the matched open parenthses and continue to next char.
            else:
                return False #return False at first occurrence of unmatched parentheses.
    if len(stack) > 0: #check for any unmatched parentheses left.
        return False
    else: #when the length of stack is 0, that means all the parentheses are matched.
        return True


# In[19]:


input_string = input("Enter a string to check balanced parenthesis: ")
if len(input_string) == 0:
    print("Error: Invalid string")
elif balanced_parentheses(input_string.strip()):
    print("The parentheses are balanced in the given string.")
else:
    print("The parentheses are not balanced in the given string.")

