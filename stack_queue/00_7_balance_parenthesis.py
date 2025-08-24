#Valid Parentheses in an Expression

# Given a string s containing three types of brackets {}, () and []. We have to determine whether the brackets are balanced.

# An expression is balanced if each opening bracket has a corresponding closing bracket of the same type, the pairs are properly ordered and no bracket closes before its matching opening bracket.

# Balanced:"[()()]{}" → every opening bracket is closed in the correct order.
# Not balanced:"([{]})" → the ] closes before the matching { is closed, breaking the nesting rule.

from collections import deque 

def is_balanced(s):
    st = deque()

    for c in s:
        if c =='{' or c=='(' or c=='[':
            st.append(c)
        
        elif c =='}' or c ==')' or c == ']':

            if not st:
                return False 
            
            top = st[-1]

            if (c == '}' and top != '{') or (c == ']' and top != '[') or (c == ')' and top != '('):
                return False 
            
            st.pop()
        
    return not st

def main():
    testCases = ["[{()}]", "[()()]{}", "(]", "([{]})"]
    for s in testCases:
        print(f'Input: {s} -> Output: {str(is_balanced(s)).lower()}')

if __name__ == '__main__':
    main()