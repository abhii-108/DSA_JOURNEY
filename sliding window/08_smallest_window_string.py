#Smallest window in a String containing all characters of other String

# Given two strings s (length m) and p (length n), the task is to find the smallest substring in s that contains all characters of p, including duplicates. If no such substring exists, return "-1". If multiple substrings of the same length are found, return the one with the smallest starting index.

# Examples: 

# Input: s = "timetopractice", p = "toc"
# Output: toprac
# Explanation: "toprac" is the smallest substring in which "toc" can be found.

# Input: s = "zoomlazapzo", p = "oza"
# Output: apzo
# Explanation: "apzo" is the smallest substring in which "oza" can be found.


def contains_all_characters(arr,p):
    (i,j) = (0,0)

    my_list={}
    min_cnt_subtstr = float('inf')

    for x in p:
        my_list[x] = my_list.get(x,0) + 1

    total_len_dict = len(my_list)
    
    while j < len(arr):

        if arr[j] in my_list:
            my_list[arr[j]] = my_list.get(arr[j],0) - 1

            if my_list.get(arr[j]) == 0 :
                total_len_dict -= 1
        
        
        if total_len_dict == 0 :
            min_cnt_subtstr = min(min_cnt_subtstr, (j-i+1))
            #print(min_cnt_subtstr)

            while total_len_dict == 0:
                if arr[i] in my_list:
                    my_list[arr[i]] = my_list.get(arr[i],0) + 1
                    
                    if  my_list.get(arr[i]) == 0 :
                        min_cnt_subtstr = min(min_cnt_subtstr, (j-i+1-1))
                        #print(min_cnt_subtstr)
                    else :
                        total_len_dict += 1
                i += 1
                # else:
                #     i += 1
        
        j += 1

    return min_cnt_subtstr
                    

print(contains_all_characters('zoomlazapzo','oza'))








