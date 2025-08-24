#Longest substring with k unique characters

#Given a string you need to print longest possible substring that has exactly k unique characters. If there is more than one substring of longest possible length, then print any one of them.


# Input: Str = "aabbcc", k = 1
# Output: 2
# Explanation: Max substring can be any one from ["aa" , "bb" , "cc"].

# Input: Str = "aabbcc", k = 2
# Output: 4
# Explanation: Max substring can be any one from ["aabb" , "bbcc"].

# Input: Str = "aabbcc", k = 3
# Output: 6
# Explanation: There are substrings with exactly 3 unique characters
#                         ["aabbcc" , "abbcc" , "aabbc" , "abbc" ]
#                         Max is "aabbcc" with length 6.

# Input: Str = "aaabbb", k = 3
# Output: -1
# Explanation: There are only two unique characters, thus show error message.

def longest_unique_substr(arr,k):
    (i,j) = (0,0)
    my_dict = {}
    my_dict_len = 0
    mx_substr_cnt = 0
    while j < len(arr):

        if arr[j] in my_dict:
            my_dict[arr[j]] = my_dict.get(arr[j], 0) + 1
        else:
            my_dict[arr[j]] = 1
            my_dict_len += 1
        

        if my_dict_len < k:
            j += 1

        elif my_dict_len == k :
            mx_substr_cnt = max(mx_substr_cnt, (j-i+1)) 

            j += 1
        
        elif my_dict_len > k :
            while my_dict_len > k:
                my_dict[arr[i]] = my_dict.get(arr[i], 0) - 1
                if my_dict.get(arr[i]) == 0:
                    del my_dict[arr[i]]
                    my_dict_len -= 1
                i += 1
            
            j += 1
        
    return mx_substr_cnt if mx_substr_cnt != 0 else -1


print(longest_unique_substr('abcbbbbccca',2))
print(longest_unique_substr("aaabbb", 3)) 
print(longest_unique_substr("abababa", 2))



        
#############################################################################################

# Program: Longest Substring with K Unique Characters
# Input: arr = 'abcbbbbccca', k = 2
# Output: 9 (Substring 'cbbbbccca' has 'c' and 'b' as 2 unique chars)

def longest_unique_substr(arr, k):
    (i, j) = (0, 0)  # Initialize window pointers: i (start), j (end)
    my_dict = {}     # Dictionary to store character frequencies in the current window arr[i...j]
    my_dict_len = 0  # Stores the count of unique characters in my_dict (len(my_dict))
    mx_substr_cnt = 0 # Stores the maximum length of substring found so far with k unique characters

    # Iterate through the array/string with the 'j' pointer (end of window)
    while j < len(arr):

        # Process the current character arr[j] and update its frequency
        if arr[j] in my_dict:
            my_dict[arr[j]] = my_dict.get(arr[j], 0) + 1 # Increment count if char exists
        else:
            my_dict[arr[j]] = 1 # Add char to dictionary with count 1 if new
            my_dict_len += 1    # Increment count of unique characters

        # Case 1: Number of unique characters is less than k
        if my_dict_len < k:
            j += 1  # Expand the window by moving 'j' to the right

        # Case 2: Number of unique characters is exactly k
        elif my_dict_len == k:
            # Found a substring with k unique characters.
            # Update max length if current window arr[i...j] is longer.
            mx_substr_cnt = max(mx_substr_cnt, (j - i + 1))
            j += 1  # Expand the window to look for other possibilities

        # Case 3: Number of unique characters is greater than k
        elif my_dict_len > k:
            # Shrink the window from the left (increment 'i') until unique char count is k or less.
            while my_dict_len > k:
                my_dict[arr[i]] = my_dict.get(arr[i], 0) - 1 # Decrement count of char arr[i]
                if my_dict.get(arr[i]) == 0: # If count of arr[i] becomes 0
                    del my_dict[arr[i]]      # Remove it from dictionary
                    my_dict_len -= 1         # Decrement count of unique characters
                i += 1  # Move 'i' to the right, shrinking the window
            
            # After shrinking, if my_dict_len becomes exactly k,
            # this specific window arr[i...j] is a candidate.
            # The existing structure will check this in the next iteration if j doesn't change the count from k,
            # or if a future window ending at a later j satisfies the condition.
            # The logic is sound as the mx_substr_cnt is updated when my_dict_len == k.
            j += 1 # Expand window to consider next element

    # If mx_substr_cnt is still 0, it means no substring with k unique chars was found.
    # Return -1 in that case as per common problem conventions, otherwise the max length.
    return mx_substr_cnt if mx_substr_cnt != 0 else -1


# Provided Test Cases
print(f"Input: arr = 'abcbbbbccca', k = 2, Output: {longest_unique_substr('abcbbbbccca', 2)}")
# Expected: 9

print(f"Input: arr = 'aaabbb', k = 3, Output: {longest_unique_substr('aaabbb', 3)}")
# Expected: -1 (String has only 2 unique characters 'a', 'b')

print(f"Input: arr = 'abababa', k = 2, Output: {longest_unique_substr('abababa', 2)}")
# Expected: 7

# New Test Cases
print(f"Input: arr = 'aabacbebebe', k = 3, Output: {longest_unique_substr('aabacbebebe', 3)}")
# Expected: 7 (for 'cbebebe')

print(f"Input: arr = 'aaaa', k = 1, Output: {longest_unique_substr('aaaa', 1)}")
# Expected: 4

print(f"Input: arr = 'aaaa', k = 2, Output: {longest_unique_substr('aaaa', 2)}")
# Expected: -1

print(f"Input: arr = 'abaccc', k = 2, Output: {longest_unique_substr('abaccc', 2)}")
# Expected: 4 (for 'accc')

# Edge Case 1: Empty string
print(f"Input: arr = '', k = 1, Output: {longest_unique_substr('', 1)}")
# Expected: -1

# Edge Case 2: k = 0
# For k=0, a non-empty substring cannot have 0 unique characters.
# An empty substring could be considered to have 0 unique chars, length 0.
# The code returns -1 if no valid non-empty substring is found and mx_substr_cnt remains 0.
print(f"Input: arr = 'abc', k = 0, Output: {longest_unique_substr('abc', 0)}")
# Expected: -1

# Edge Case 3: k > number of actual unique characters in string
print(f"Input: arr = 'abc', k = 4, Output: {longest_unique_substr('abc', 4)}")
# Expected: -1

# Edge Case 4: k is larger than string length (but string might have few unique chars)
print(f"Input: arr = 'a', k = 2, Output: {longest_unique_substr('a', 2)}")
# Expected: -1

# Edge Case 5: k = 1, multiple characters
print(f"Input: arr = 'aabbc', k = 1, Output: {longest_unique_substr('aabbc', 1)}")
# Expected: 2 (for 'aa' or 'bb' or 'c' - wait, it should be longest, so 'aa' or 'bb'. The code handles this.)
# 'aa' -> len 2. 'bb' -> len 2. 'c' -> len 1. Max is 2.
