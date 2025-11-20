##Square integers and floats"""


def square(n):
    """Takes a number (integer or float) and returns
its square -- i.e., the number to the 2nd power
"""
    return n ** 2

print(square(3))
print(square(3.14))
print("#"* 100)

def largest(s):
    """Takes a sequence, and returns the largest
element (as defined by >) from the sequence.
"""
    if not s:
        return None

    output = s[0]

    for one_item in s[1:]:
        if one_item > output:
            output = one_item

    return output

print(largest([1,2,3,4,10,5,6])) ## pass list 
print(largest((1,2,3,4,10,5,6))) ## pass tuple 

print(largest(('A','m','C','Z')))
print(largest(['A','m','C','Z']))


##Longest word in file-like"""


def longest_word(f):
    """Takes a file-like object, and returns the longest
        word it finds.
"""
    longest_word = ''

    for one_line in f:
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word

    return longest_word

print('-'*100)

def even_odd_sums(numbers):
    odd_sum = 0
    even_sum = 0 

    for num in numbers:
        if num % 2 == 0:
            even_sum += num 
        else:
            odd_sum += num 

    return [odd_sum, even_sum] 