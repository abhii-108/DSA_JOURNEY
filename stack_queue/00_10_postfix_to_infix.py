# #Postfix to Infix
# Postfix to infix conversion involves transforming expressions where operators follow their operands (postfix notation) into standard mathematical expressions with operators placed between operands (infix notation). This conversion improves readability and understanding.

# Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands. 
# Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands. 
# Examples: 

# Input: abc++
# Output: (a + (b + c))
# Explanation: Infix expression is  (a + (b + c)) for expression abc++

# Input: ab*c+
# Output: ((a*b)+c)
# Explanation: Infix expression is  ((a*b)+c) for expression ab*c+

# Input: abc+*d/
# Output: (((a * (b + c))) / d)
# Explanation: Infix expression is (((a * (b + c)))/d) for expression abc+*d/

def postfix_to_infix(s):
    st=[]

    for i in range(len(s)):
        if s[i].isalnum():
            st.append(s[i])

        else:
            t1 = st.pop()
            t2 = st.pop()
            conc = f'({t2}{s[i]}{t1})'
            st.append(conc)
    
    return st[-1]

if __name__ == '__main__': 

    exp = "ab*c+"
    exp2="AB-DE+F*/"
    print(postfix_to_infix(exp.strip()))
    print(postfix_to_infix(exp2.strip()))