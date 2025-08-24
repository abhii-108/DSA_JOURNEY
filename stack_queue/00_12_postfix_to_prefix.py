# #Postfix to Prefix Conversion

# Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. Simply of the form (operand1 operand2 operator). 
# Example : AB+CD-* (Infix : (A+B) * (C-D) )

# Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
# Example : *+AB-CD (Infix : (A+B) * (C-D) )

# Problem Statement
# Given a Postfix expression, convert it into a Prefix expression.

# Instead of converting Postfix → Infix → Prefix, we can directly convert Postfix → Prefix.
# This method is both efficient (fewer steps) and intuitive, since computers naturally evaluate expressions in Postfix form.

# Examples: 

# Input :  Postfix : AB+CD-*
# Output : Prefix :  *+AB-CD
# Explanation : Postfix to Infix : (A+B) * (C-D)
#               Infix to Prefix :  *+AB-CD

# Input :  Postfix : ABC/-AK/L-*
# Output : Prefix :  *-A/BC-/AKL
# Explanation : Postfix to Infix : ((A-(B/C))*((A/K)-L))
#               Infix to Prefix :  *-A/BC-/AKL  


def postfix_to_prefix(s):
    st = []
    for i in range(len(s)):
        if s[i].isalnum():
            st.append(s[i])
        
        else:
            t1 = st.pop()
            t2 = st.pop()
            con = s[i] + t2 + t1
            st.append(con)
    
    return st[-1]




if __name__ == '__main__': 

    exp = "AB+CD-*"
    exp2="ABC/-AK/L-*"
    print(postfix_to_prefix(exp.strip()))
    print(postfix_to_prefix(exp2.strip()))