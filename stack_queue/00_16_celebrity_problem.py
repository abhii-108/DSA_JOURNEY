#The Celebrity Problem


# Given a square matrix mat[][] of size n x n, where mat[i][j] == 1 means person i knows person j, and mat[i][j] == 0 means person i does not know person j, the objective is to find the celebrity.

# A celebrity is defined as someone who:

# Is known by everyone else
# Does not know anyone (except themselves)

# Return the index of the celebrity if one exists, otherwise return -1.

# Note:

# Use 0-based indexing
# It is guaranteed that mat[i][i] == 1 for all i

# Input: mat[][] = [[1, 1, 0], 
#                   [0, 1, 0], 
#                   [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

# Input: mat[][] = [[1, 1], 
#                   [1, 1]]
# Output: -1
# Explanation: The two people at the party both know each other. None of them is a celebrity.

# Input: mat[][] = [[1]]
# Output: 0

######### Navie Approach ############# 

def celebrity(mat):

    n = len(mat)

    know_me = [0] * n 
    i_know = [0] * n 


    for i in range(n):
        for j in range(n):

            if mat[i][j]  == 1:

                know_me[j] += 1
                i_know[i] += 1
            
    
    for i in range(n):
        if (know_me[i] == n-1) and (i_know[i] == 0):
            return i
    
    return -1 



######### optimized Approach ############# 

def celebrity_op(mat):

    n = len(mat)

    top = 0 
    down = n-1


    while top < down:

        if mat[top][down] == 1 :
            top += 1
        
        elif mat[down][top] == 1:
            down -= 1

    celebrity_candidate = top

    for i in range(n):
        print(f'inside for {i}')
        # A celebrity knows no one, so mat[celebrity_candidate][i] must be 0 for all i (where i != candidate).
        if mat[top][i] == 1 and i != top:
            return -1  # Fails the first condition.
        
        # Everyone else must know the celebrity, so mat[i][celebrity_candidate] must be 1 for all i (where i != candidate).
        if mat[i][top] == 0 and i != top:
            return -1  # Fails the second condition
    
    return celebrity_candidate 

if __name__ == "__main__":
    mat = [[1, 1, 1, 0],
           [0, 0, 0, 0],
           [0, 1, 0, 0],
           [1, 1, 0, 0]]
    print(celebrity_op(mat))

