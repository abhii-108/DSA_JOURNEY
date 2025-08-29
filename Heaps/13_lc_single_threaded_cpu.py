## Single-Threaded CPU

# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.


# Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# Explanation: The events go as follows: 
# - At time = 1, task 0 is available to process. Available tasks = {0}.
# - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
# - At time = 2, task 1 is available to process. Available tasks = {1}.
# - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
# - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
# - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
# - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
# - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
# - At time = 10, the CPU finishes task 1 and becomes idle.


import heapq
from typing import List

def getOrder(tasks: List[List[int]]) -> List[int]:

    ## length of array 
    n = len(tasks)

    #Enumerate the list to pair each inner list with its original index.
    #The result will be a list of tuples like (index, sublist).
    indexed_list = list(enumerate(tasks))
    #print(indexed_list)  --> [(0, [1, 2]), (1, [2, 4]), (2, [3, 2]), (3, [4, 1])] --> [(0, [2, 4]), (1, [1, 2]), (2, [3, 2]), (3, [4, 1])]

    #Sort the indexed list.
    #    The 'key' argument tells Python how to sort. We're sorting based on
    #    the first element of the sublist, which is the second item in our tuple (item[1]).
    #    So, we use a lambda function to access that element (item[1][0]).
    
    sorted_list = sorted(indexed_list, key=lambda item: item[1][0])
    #print(sorted_list)  --> (1, [1, 2]), (0, [2, 4]), (2, [3, 2]), (3, [4, 1])]
    ## list is sorted in tuple (index pos, [starttime, process_time])

    res = []
    min_heap = []

    curr_time = 0 
    idx = 0
    while idx < n or min_heap:

        if not min_heap and curr_time < sorted_list[idx][1][0]:
            curr_time = sorted_list[idx][1][0]

        
        while idx < n and sorted_list[idx][1][0] <= curr_time:
            heapq.heappush(min_heap,(sorted_list[idx][1][1], sorted_list[idx][0]))  ## pushing a pair of value {duration time of process, original index of task} in heap 
            idx += 1

        process_time, task_id = heapq.heappop(min_heap)

        curr_time += process_time

        res.append(task_id)
    
    return res 

print(getOrder([[1,2],[2,4],[3,2],[4,1]]))