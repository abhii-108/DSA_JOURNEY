#Prefix to Infix Conversion
# Infix : An expression is called the Infix expression if the operator appears in between the operands in the expression. Simply of the form (operand1 operator operand2). 
# Example : (A+B) * (C-D)

# Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
# Example : *+AB-CD (Infix : (A+B) * (C-D) )

# Given a Prefix expression, convert it into a Infix expression. 
# Computers usually does the computation in either prefix or postfix (usually postfix). But for humans, its easier to understand an Infix expression rather than a prefix. Hence conversion is need for human understanding.

# Examples: 

# Input :  Prefix :  *+AB-CD
# Output : Infix : ((A+B)*(C-D))

# Input :  Prefix :  *-A/BC-/AKL
# Output : Infix : ((A-(B/C))*((A/K)-L))

def prefix_to_infix(s):
    st = []

    for i in range(len(s)-1,-1,-1):

        if s[i].isalnum():
            st.append(s[i])
        
        else:
            t1=st.pop()
            t2=st.pop()
            con = '('+t1+s[i]+t2+')'
            st.append(con)
    
    return st[-1]


if __name__ == '__main__': 

    exp = "*+AB-CD"
    exp2="*-A/BC-/AKL"
    print(prefix_to_infix(exp.strip()))
    print(prefix_to_infix(exp2.strip()))