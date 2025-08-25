# ## Find K Closest Points to the Origin

# Given an array of points where each point is represented as points[i] = [xi, yi] on the X-Y plane and an integer k. The task is to find k closest points to the origin(0,0) in any order.

# input: k = 3, points = [[1, 3], [-2, 2], [5, -1], [3, 2], [1, 1]]
# Output: [[1, 1], [-2, 2], [1, 3]]
# Explanation: The Euclidean distances from the origin are:
# Point (1, 3) = sqrt(10)
# Point (-2, 2) = sqrt(8)
# Point (5, -1) = sqrt(26)
# Point (3, 2) = sqrt(13)
# Point (1, 1) = sqrt(2)

# The three closest points to the origin are [1, 1], [-2, 2] and [1, 3].

# Input: k = 1, points = [[2, 4], [-1, -1], [0, 0]]
# Output: [[0, 0]]
# Explanation: The Euclidean distances from the origin are:
# Point (2, 4) = sqrt(20)
# Point (-1, -1) = sqrt(2)
# Point (0, 0) = sqrt(0)

# The closest point to origin is [0, 0].

import heapq 

def closest_point_origin(arr, k):

    max_heap = []

    for rows in range(len(arr)):
        dist_origin = (arr[rows][0] * arr[rows][0]) + (arr[rows][1] * arr[rows][1])

        heapq.heappush(max_heap,(-dist_origin, [arr[rows][0], arr[rows][1]]))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    res = []
    while max_heap:
        dist_origin, points = heapq.heappop(max_heap)

        res.append(points)

    return res 

if __name__ == "__main__":
    arr = [[1, 3], [-2, 2], [5, -1], [3, 2], [1, 1]]
    arr2 = [[2, 4], [-1, -1], [0, 0]]


    # Function call
    print("#Closest K Elements in a Array", closest_point_origin(arr,3))
    print("#Closest K Elements in a Array", closest_point_origin(arr2, 1))


    

    