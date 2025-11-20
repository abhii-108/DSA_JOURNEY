import operator

def alphabetize_names(list_of_dicts):
      
    """Take a list of dicts describing people,
    each with first/last/email as keys.

    Return a new list of dicts,
    sorted first by last name and then by first name.

    If passed an empty list, then return an empty list.
    """
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))



PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]

print(alphabetize_names(PEOPLE))

# # key=operator.itemgetter('last', 'first') 
# # creates a function that, when applied to a dictionary, extracts the values associated with the keys 'last' and then 'first'.
# # For each dictionary, this key function returns a tuple of two values.
# # Dictionary Itemitemgetter('last', 'first') 
# # Output (Key Tuple)
# # Reuven Lerner('Lerner', 'Reuven')
# # Donald Trump('Trump', 'Donald')
# # Vladimir Putin('Putin', 'Vladimir')

# # The sorted() function then sorts the original list based on these key tuples. Python sorts tuples lexicographically (one element at a time):

# # Primary Sort: It compares the first element of each tuple ('last' name).

# # Secondary Sort: If the first elements are identical (e.g., two people with the same last name), it then compares the second element ('first' name) to break the tie.


print('-'*100)

def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


def sort_by_vowel_count(words):
    """Given a list of strings (words), return
a list of those words sorted by the number of vowels
they contain.
"""
    return sorted(words, key=by_vowel_count)