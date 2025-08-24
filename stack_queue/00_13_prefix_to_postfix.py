# #Prefix to Postfix Conversion
# Given a Prefix expression, convert it into a Postfix expression. 
# Conversion of Prefix expression directly to Postfix without going through the process of converting them first to Infix and then to Postfix is much better in terms of computation and better understanding the expression (Computers evaluate using Postfix expression). 

# let's discuss about Prefix and Postfix notation:

# Prefix: An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
# Example : *+AB-CD (Infix : (A+B) * (C-D) )

# Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. Simply of the form (operand1 operand2 operator). 
# Example : AB+CD-* (Infix : (A+B * (C-D) )

# Note : Follow the link for prefix to postfix online convertor.

# Examples: 

# Input :  Prefix :  *+AB-CD
# Output : Postfix : AB+CD-*
# Explanation : Prefix to Infix :  (A+B) * (C-D)
#                          Infix to Postfix :  AB+CD-*

# Input :  Prefix :  *-A/BC-/AKL
# Output : Postfix : ABC/-AK/L-*
# Explanation : Prefix to Infix :  (A-(B/C))*((A/K)-L)
#                          Infix to Postfix : ABC/-AK/L-* 


def prefix_to_postfix(s):
    st = []

    for i in range(len(s)-1,-1,-1):

        if s[i].isalnum():
            st.append(s[i])
        
        else:
            t1 = st.pop()
            t2 = st.pop()
            con = t1 + t2 + s[i]
            st.append(con)
    
    return st[-1]

if __name__ == '__main__': 

    exp = "*+AB-CD"
    exp2="*-A/BC-/AKL"
    print(prefix_to_postfix(exp.strip()))
    print(prefix_to_postfix(exp2.strip()))