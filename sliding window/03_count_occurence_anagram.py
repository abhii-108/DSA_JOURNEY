#Count Occurences of Anagrams
# Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

# Input: txt = "forxxorfxdofr", pat = "for"
# Output: 3
# Explanation: for, orf and ofr appears in the txt, hence answer is 3.

# Input: txt = "aabaabaa", pat = "aaba"
# Output: 4
# Explanation: aaba is present 4 times in txt.

def find_anagram_count(arr,word):

    my_dict = {} # creating blank dictionary 
    dict_len = 0

    i = 0 
    j = 0 
    anagram_count = 0 

    for x in word:
        if x in my_dict:
            my_dict[x] += 1
        else :
            my_dict[x] = 1
    
    dict_len = len(my_dict)


    while j < len(arr):
        # Calcuation 
        if arr[j] in my_dict:
            my_dict[arr[j]] -= 1

            if my_dict[arr[j]] == 0:
                dict_len -= 1
         
        if (j-i+1) < len(word):
            j += 1
        
        elif (j-i+1) == len(word):

            if dict_len == 0:
                anagram_count += 1
                # my_dict[arr[i]] += 1
                # dict_len += 1

            if arr[i] in my_dict and my_dict[arr[i]] == 0: # need to check if arr[i] is present or not if not present then diretly 
                if my_dict[arr[i]] == 0:
                    dict_len += 1
                my_dict[arr[i]] += 1
                
                #print(f' dict_len after  increment ={dict_len} ')
            
            i += 1
            j += 1
    
    return anagram_count





print(find_anagram_count('forxxorfxdofr','for'))
print(find_anagram_count('aabaabaa','aaba'))
            



