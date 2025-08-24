# #Infix to Postfix Expression
# Write a program to convert an Infix expression to Postfix form.

# Infix expression: The expression of the form "a operator b" (a + b) i.e., when an operator is in-between every pair of operands.
# Postfix expression: The expression of the form "a b operator" (ab+) i.e., When every pair of operands is followed by an operator.

# Examples:

# Input: s = "A*(B+C)/D"
# Output: ABC+*D/

# Input: s = "a+b*(c^d-e)^(f+g*h)-i"
# Output: abcd^e-fgh*+^*+i- 

def prec(c):
    if c == '^':
        return 3 
    
    elif c in ['*', '/']:
        return 2 
    elif c in ['+', '-']:
        return 1 
    else:
        return -1 
    
def infix_to_postfix(s):
    st = []
    ans = ''

    for x in s :
        if x.isalnum():
            ans += x 
        
        elif x == '('  :
            st.append(x)
        elif x == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()
        else:
            while st and prec(x) <= prec(st[-1]):
                
                ans += st.pop()
            st.append(x)

    while st:
        ans += st.pop()
    
    return ans 

if __name__ == '__main__':
    exp = 'a+b*(c^d-e)^(f+g*h)-i'
    print(infix_to_postfix(exp))


#abcd^e-fgh*+^*+i-
#abcd^e-fgh*+^*+i-