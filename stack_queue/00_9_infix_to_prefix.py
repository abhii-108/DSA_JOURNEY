# #Infix To Prefix Notation
# Given an infix expression consisting of operators (+, -, *, /, ^) and operands (lowercase characters), the task is to convert it to a prefix expression.

# Infix Expression: The expression of type a 'operator' b (a+b, where + is an operator) i.e., when the operator is between two operands.

# Prefix Expression: The expression of type 'operator' a b (+ab where + is an operator) i.e., when the operator is placed before the operands.

# Input: a*b+c/d
# Output: +*ab/cd 

# Input: (a-b/c)*(a/k-l)
# Output: *-a/bc-/akl

def prec(c):
    if c == '^':
        return 3 
    
    elif c in ['*', '/']:
        return 2 
    elif c in ['+', '-']:
        return 1 
    else:
        return -1 
    
def reverse_expression(s):

    infix_exp = s[::-1]
    modified_characters=[]
    #print(infix_exp)
    for key, val in enumerate(infix_exp):
        if val == '(':
            modified_characters.append(')')
            
        elif val == ')':
             modified_characters.append('(')
        else:
             modified_characters.append(val)
        
    return ''.join(modified_characters)



def infix_to_prefix(s):

    sr = reverse_expression(s)
    st = []
    res = ''
    for i in range(len(sr)):
        if sr[i].isalnum():
            res += sr[i]

        elif sr[i] == '(':
            st.append(sr[i])

        elif sr[i] == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        
        else:
            while st and prec(st[-1]) >= prec(sr[i]):
                res += st.pop()
            st.append(sr[i])
    
    while st:
        res += st.pop()
    print(res)
    return res[::-1] 


print(infix_to_prefix('(a-b/c)*(a/k-l)'))
