# ## LC Minimum Knight Moves
# In this problem, we are given an infinite chess board that can be imagined as an endless grid with coordinates ranging from negative infinity to positive infinity. We have a chess piece—a knight—placed at the origin [0, 0] of this grid. The objective is to calculate the minimum number of moves that the knight must make to reach a specific square [x, y] on the chessboard.

# A knight in chess moves in an L-shape: it can move two squares in one direction (either horizontally or vertically) and then make a 90-degree turn to move one square in a perpendicular direction. This gives the knight a total of eight possible moves at any given point.

# The problem requires us to determine the least number of moves necessary to get the knight from its starting position [0, 0] to any target coordinates [x, y]. The question assures that it is always possible to reach the target square.


from collections import deque

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
    
if __name__ == "__main__":
    # Example test cases:
    op = Solution()
    print("Example 1:", op.minKnightMoves(2, 1))  # Expected: 1
    print("Example 2:", op.minKnightMoves(5, 5))  # Expected: 4 (one possible answer)
    print("Example 3:", op.minKnightMoves(0, 0))  # Expected: 0