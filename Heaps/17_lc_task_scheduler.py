# ## Task Scheduler

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

from typing import List 
import heapq
from collections import Counter

def leastInterval(tasks: List[str], n: int) -> int:

    task_counts  = Counter(tasks)
    max_heap = []
    for task, count in task_counts.items():
        #print(f" ({-count}, {task})")
        heapq.heappush(max_heap,(-count))

    cpu_interval = 0
    print(f' len for heap is {len(max_heap)}')
    while max_heap:
        temp = []
        for i in range(n+1):
            if len(max_heap) > 0:
                freq = heapq.heappop(max_heap)
                temp.append(freq+1)
        
        for x in temp:
            if x < 0 :
                heapq.heappush(max_heap,x)
        
        if len(max_heap) == 0:
            cpu_interval += len(temp)
        else:
            cpu_interval += n+1

    return cpu_interval


print(leastInterval(["A","A","A","B","B","B"], 2))