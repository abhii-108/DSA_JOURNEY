### stock span problem 
## The stock span problem is a financial problem where we have a series of daily price quotes for a stock denoted by an array arr[] and the task is to calculate the span of the stock's price for all days. 

#The span of the stock's price on ith day represents the maximum number of consecutive days leading up to ith day (including the current day) where the stock's price was less than or equal to its price on day i.

# Input: arr[] = [10, 4, 5, 90, 120, 80]
# Output: [1, 1, 2, 4, 5, 1]

from collections import deque

def stock_span(arr):

    stack = []

    op = [0] * len(arr)

    #LSR with index position
    # for i in range(0, len(arr)):

    #     if len(stack) == 0:
    #         op[i] = -1 
        
    #     elif stack[-1][1] > arr[i]:
    #         #sprint(stack[-1][1])
    #         op[i] = stack[-1][0]
        
    #     else:
    #         while (len(stack) != 0) and (stack[-1][1] <= arr[i]):
    #             stack.pop()
            
    #         if len(stack) == 0:
    #             op[i] = -1
    #         else:
    #             op[i] = stack[-1][0]

    #     stack.append([i,arr[i]])  #we are appending the position of i and value as a list in stack. 

    for i, val in enumerate(arr):

        if not stack:
            op[i] = -1

        elif stack[-1][0] > val:
            op[i] = stack[-1][1]

        else:
            while stack and stack[-1][0] <= val:
                stack.pop()
            
            if stack:
                op[i] = stack[-1][1]
            else:
                op[-1] = -1

        stack.append([val,i])
    
    for i in range(0,len(arr)):
        op[i] = i - op[i]
    
    return op 


print(stock_span([10, 4, 5, 90, 120, 80]))
print(stock_span([100, 80, 60, 70, 60, 65, 85]))


# [1, 1, 2, 4, 5, 1]
# [1, 1, 1, 2, 1, 2, 6]



#####################################################################################

# from collections import deque

# def stock_span(prices):
#     """
#     Calculates the stock span for each day in a given list of daily prices.
#     The span of a stock's price today is the maximum number of consecutive days
#     (starting from today and going backward) for which the price of the stock
#     was less than or equal to today's price.

#     This function uses a monotonic stack to find the Previous Greater Element (PGE)
#     for each price.

#     Args:
#         prices: A list of integers representing the daily stock prices.

#     Returns:
#         A list of integers where each element is the span for the corresponding day's price.
#     """
#     n = len(prices)
#     # Hint: Handle empty or single-element price lists.
#     if n == 0:
#         return []
#     if n == 1:
#         return [1] # A single day always has a span of 1.

#     stack = deque() # Monotonic stack to store (index, price) pairs.
#                     # It maintains elements in decreasing order of price (from bottom to top).

#     pge_index = [0] * n # Array to store the index of the Previous Greater Element (PGE) for each price.
#                         # This array will essentially be similar to 'op' in your original code.

#     # --- Step 1: Find the index of the Previous Greater Element (PGE) for each price ---
#     # Hint: Iterate from left to right. Maintain a monotonic decreasing stack.
#     # When a price is encountered, pop elements from stack that are less than or equal to current price.
#     # The top of stack (if not empty) will be the PGE.
#     for i in range(n):
#         # While stack is not empty AND the price at the top of the stack is less than or equal to current price:
#         # These elements are "smaller" and thus cannot be the PGE for future elements
#         # that are greater than or equal to the current price. They are superseded.
#         while stack and stack[-1][1] <= prices[i]:
#             stack.pop() # Pop elements that are smaller or equal to the current price.

#         # After popping, if the stack is empty, it means no greater element exists to the left.
#         # In this case, the PGE is considered to be at an imaginary index -1.
#         if not stack:
#             pge_index[i] = -1
#         else:
#             # Otherwise, the top element of the stack is the Previous Greater Element.
#             pge_index[i] = stack[-1][0] # Store its index.

#         # Push the current price's index and price onto the stack.
#         # The stack maintains a decreasing order of prices.
#         stack.append([i, prices[i]])

#     # --- Step 2: Calculate the span for each day ---
#     # Hint: The span for a day 'i' is simply the current index 'i' minus the index of its PGE.
#     # If PGE was -1, it means all previous elements were smaller, so the span is (i - (-1)) = i + 1.
#     span_result = [0] * n
#     for i in range(n):
#         span_result[i] = i - pge_index[i]

#     return span_result

# --- Test Cases ---

print(f"Prices: [10, 4, 5, 90, 120, 80], Spans: {stock_span([10, 4, 5, 90, 120, 80])}\nExpected: [1, 1, 2, 4, 5, 1]")
print(f"Prices: [100, 80, 60, 70, 60, 75, 85], Spans: {stock_span([100, 80, 60, 70, 60, 75, 85])}\nExpected: [1, 1, 1, 2, 1, 4, 6]")
print(f"Prices: [1, 2, 3, 4, 5], Spans: {stock_span([1, 2, 3, 4, 5])}\nExpected: [1, 2, 3, 4, 5] (Monotonically increasing)")
print(f"Prices: [5, 4, 3, 2, 1], Spans: {stock_span([5, 4, 3, 2, 1])}\nExpected: [1, 1, 1, 1, 1] (Monotonically decreasing)")
print(f"Prices: [7, 7, 7, 7], Spans: {stock_span([7, 7, 7, 7])}\nExpected: [1, 2, 3, 4] (All equal)")
print(f"Prices: [10, 20, 15, 30, 25], Spans: {stock_span([10, 20, 15, 30, 25])}\nExpected: [1, 2, 1, 4, 1]")
print(f"Prices: [], Spans: {stock_span([])}\nExpected: [] (Edge case: Empty list)")
print(f"Prices: [5], Spans: {stock_span([5])}\nExpected: [1] (Edge case: Single element list)")



# The Stock Span problem asks us to find, for each day, the number of consecutive days before it (including itself) whose prices were less than or equal to the current day's price.

# The core idea is to find the Previous Greater Element (PGE) for each stock price. Once we know the index of the first price to the left that is greater than the current price, the span is simply the difference between the current day's index and the PGE's index.

# Let's break down the stock_span function:

# Initialization and Edge Cases:

# n = len(prices): Get the number of days.
# if n == 0: return [] or if n == 1: return [1]: Handle empty or single-day scenarios directly. An empty list has no spans, and a single day always has a span of 1.
# Monotonic Stack (stack):

# stack = deque(): A deque (double-ended queue) is used as a stack. It will store tuples of (index, price).
# Crucially, this stack will maintain elements in monotonically decreasing order of prices. This means stack[-1][1] (top element's price) will always be less than or equal to stack[-2][1] (second-to-top element's price), and so on.
# Finding Previous Greater Element (PGE) - pge_index array:

# pge_index = [0] * n: This array will store the index of the PGE for each day.
# Iterate from left to right (i from 0 to n-1):
# while stack and stack[-1][1] <= prices[i]: stack.pop(): This is the heart of the monotonic stack. For the current price prices[i]:
# We look at the top element of the stack.
# If the top element's price (stack[-1][1]) is less than or equal to the current prices[i], it means this element on the stack (and any elements below it that are also less than or equal to prices[i]) cannot be the PGE for prices[i] or any future elements that are greater than prices[i]. prices[i] effectively "overshadows" them. So, we pop() them off the stack.
# This loop continues until either the stack becomes empty or we find an element on the stack whose price is greater than prices[i].
# if not stack: pge_index[i] = -1: If the stack becomes empty after popping, it means there is no element to the left of prices[i] that is greater than prices[i]. In this case, we use a sentinel value like -1 to indicate that prices[i] is the greatest element seen so far from the beginning of the array.
# else: pge_index[i] = stack[-1][0]: If the stack is not empty, the element at the top of the stack (stack[-1]) is the Previous Greater Element for prices[i]. We store its index (stack[-1][0]).
# stack.append([i, prices[i]]): Finally, push the current day's (index, price) onto the stack. This maintains the monotonic decreasing property.
# Calculating the Span:

# span_result = [0] * n: Initialize an array to store the final span values.
# for i in range(n): span_result[i] = i - pge_index[i]: This is the final calculation.
# For each day i, its span is the current index i minus the index of its PGE (pge_index[i]).
# Why i - pge_index[i]?
# If pge_index[i] is -1 (meaning prices[i] is the largest so far), the span is i - (-1) = i + 1. This correctly counts all i+1 elements from index 0 to i.
# If pge_index[i] is, say, k, it means prices[k] is the first greater element to the left. All elements from index k+1 to i (inclusive) are less than or equal to prices[i]. The count of these elements is i - (k+1) + 1 = i - k. So, i - pge_index[i] correctly gives this count.
# Return span_result: The array containing the calculated spans for each day.