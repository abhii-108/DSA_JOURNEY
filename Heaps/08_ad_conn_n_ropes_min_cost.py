# ## Connect n ropes with minimum cost
# Given an array arr[] of rope lengths, connect all ropes into a single rope with the minimum total cost. The cost to connect two ropes is the sum of their lengths.

# Examples:

# Input: arr[] = [4, 3, 2, 6]
# Output: 29
# Explanation: We can connect the ropes in following ways.
# 1) First connect ropes of lengths 2 and 3. Which makes the array [4, 5, 6]. Cost of this operation 2 + 3 = 5. 
# 2) Now connect ropes of lengths 4 and 5. Which makes the array [9, 6]. Cost of this operation 4 + 5 = 9.
# 3) Finally connect the two ropes and all ropes have connected. Cost of this operation 9 + 6 =15. Total cost is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. 

# Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first (we get three rope of 3, 2 and 10), then connect 10 and 3 (we get two rope of 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.

# Input: arr[] = [10]
# Output: 0
# Explanation: Since there is only one rope, no connections are needed, so the cost is 0.
import heapq

def connect_ropes(arr):

    heapq.heapify(arr)
    total_cost = 0
    while len(arr) > 1:
        
        R1 = heapq.heappop(arr)
        R2 = heapq.heappop(arr)

        conn_rope = R1 + R2 
        total_cost += conn_rope

        heapq.heappush(arr,conn_rope)

    
    return total_cost

if __name__ == "__main__":
  
    arr = [4, 3, 2, 6]
    print(connect_ropes(arr))