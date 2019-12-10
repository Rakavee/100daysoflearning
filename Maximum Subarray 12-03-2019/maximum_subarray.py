from sys import maxsize 
def maxSubArraySum(nums): 
    max_sum = -maxsize - 1
    current_sum = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(len(nums)): 
  
        current_sum += nums[i] 
  
        if current_sum > max_sum: 
            max_sum = current_sum 
            start = s 
            end = i
  
        if current_sum < 0: 
            current_sum = 0
            s = i+1
  
    print("Start: ",start," End: ",end," Sum: ",max_sum)


nums = [-1,-2,-3]
maxSubArraySum(nums)