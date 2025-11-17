def mysum(*numbers):
    output = 0 

    for num in numbers:
        output += num 
    
    return output

print(mysum(10,20,30,10))

def mysum2(*numbers):
    output = 0 

    for num in numbers:
        output += num 
    
    return output

print(mysum2(*[10,20,30,100]))
print(mysum2(*(100,200,300,100),100,200))

######### 2 #######################
def myavg(*numbers):
    output = 0 

    for num in numbers:
        output += num 
    
    return output/len(numbers)   


print(myavg(*[10,20,30,100]))


######### 4 #######################
def min_max_avg_len(*words):
    # min_size = float('inf')
    # max_size = 0
    # avg_size = 0 

    # for word in words:
    #     min_size = min(min_size, len(word))
    #     max_size = max(max_size, len(word))
    #     avg_size += len(word)
    
    # return (min_size, max_size, (avg_size/len(words)))

    words_list = [len(word)for word in words]
    return min(words_list), max(words_list), sum(words_list)/len(words_list)


print(min_max_avg_len(*['Hello','welcometo','facebook']))