## Longest Substring Without Repeating Characters

#Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 


# Input: s = "aaa"
# Output: 1
# Explanation: The longest substring without repeating characters is "a"

# Input: s = "abcdefabcbb"
# Output: 6
# Explanation: The longest substring without repeating characters is "abcdef".


def longest_unique_substr(arr):
    i = 0 
    j = 0 

    my_dict = {}
    mx_long_substr=0

    while j < len(arr):

        if arr[j] in my_dict:
            my_dict[arr[j]] = my_dict.get(arr[j], 0) + 1
        else:
            my_dict[arr[j]] = 1

        
        if (j-i+1) == len(my_dict):
            mx_long_substr = max(mx_long_substr, (j-i+1))
            
        
        elif (j-i+1) != len(my_dict):
            while (j-i+1) != len(my_dict):
                my_dict[arr[i]] = my_dict.get(arr[i], 0) - 1
                if my_dict.get(arr[i]) == 0:
                    del my_dict[arr[i]]
                i += 1
            
        j += 1
    
    return mx_long_substr
        

print(longest_unique_substr('abcdefabcbb'))


            
