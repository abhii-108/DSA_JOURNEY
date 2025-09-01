# ## LC Minimum Knight Moves
# In this problem, we are given an infinite chess board that can be imagined as an endless grid with coordinates ranging from negative infinity to positive infinity. We have a chess piece—a knight—placed at the origin [0, 0] of this grid. The objective is to calculate the minimum number of moves that the knight must make to reach a specific square [x, y] on the chessboard.

# A knight in chess moves in an L-shape: it can move two squares in one direction (either horizontally or vertically) and then make a 90-degree turn to move one square in a perpendicular direction. This gives the knight a total of eight possible moves at any given point.

# The problem requires us to determine the least number of moves necessary to get the knight from its starting position [0, 0] to any target coordinates [x, y]. The question assures that it is always possible to reach the target square.


from collections import deque
from typing import List

class Solution:
    def minKnightMoves(self, x:int, y:int ) -> int:

        ## initilaize a queue and start with knight initial position (0,0)

        q = deque([(0,0)])

        moves_count = 0 

        visited = {(0,0)}

        directions = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

        while q:

            for _ in range(len(q)):

                curr_i, curr_j = q.popleft()

                # If the target position is reached, return the number of moves.

                if curr_i == x and curr_j == y:
                    return moves_count
                
                for delta_i, delta_j in directions:
                    new_i, new_j = curr_i + delta_i , curr_j + delta_j 

                    if (new_i,new_j) not in visited:
                        visited.add((new_i, new_j))
                        q.append((new_i, new_j))
            
            
            moves_count += 1
        
        return -1 


class Solution_two:
    def minKnightMoves_2(self, n:int, knightPos:List, targetPos:list ) -> int:
    ## first converting the n*n chess in matrix to 0,0 
        src_x = n - knightPos[1]
        src_y = knightPos[0] - 1 

        target_x = n - targetPos[1]
        target_y = targetPos[0] - 1

        directions = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
        moves_count= 0 
        queue = deque([(src_x, src_y)])

        # Visited array to keep track of visited squares
        visited = [[0 for _ in range(n)] for _ in range(n) ]

        # [
        # [0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0]
        # ]
        visited[src_x][src_y] = 1

        while queue: 
            q_len = len(queue)

            for _ in range(q_len):
                
                curr_x, curr_y = queue.popleft()

                if (curr_x == target_x and curr_y == target_y):
                    return moves_count 
                
                for delta_i, delta_j in directions:

                    new_i = delta_i + curr_x 
                    new_j = delta_j + curr_y 

                    if (new_i >= 0 and new_j >= 0 and new_i < n and new_j < n and visited[new_i][new_j] == 0 ):
                        visited[new_i][new_j] = 1
                        queue.append((new_i, new_j))
            
            moves_count += 1
        
        return moves_count


               

if __name__ == "__main__":
    # Example test cases:
    op = Solution()
    print("Example 1:", op.minKnightMoves(2, 1))  # Expected: 1
    print("Example 2:", op.minKnightMoves(5, 5))  # Expected: 4 (one possible answer)
    print("Example 3:", op.minKnightMoves(0, 0))  # Expected: 0


    op2 = Solution_two()
    print("Example 2.1:", op2.minKnightMoves_2(3,[3, 3],[1,2])) 
    print("Example 2.2:", op2.minKnightMoves_2(6, [4, 5],[1,1])) 