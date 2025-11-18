def pl_sentence(sentence):
    op = []

    for word in sentence.split():
        if word[0] in 'aeiou':
            op.append(f'{word}way')
    
        else:
            op.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(op)


print(pl_sentence('this is a test'))


def word_per_line(filename):
    """Given a text file, return a sentence from the nth
word for line n, for each of the first 10 lines.
"""
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return ' '.join(output)


def transpose_strings(list_of_words):
    

    new_val = [s.split() for s in list_of_words]
    output = [' '.join(t) for t in zip(*new_val)]
    print(output)


transpose_strings(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])


list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C']

# Zipping them pairs (1, 'A'), (2, 'B'), (3, 'C')
zipped = list(zip(list1, list2))
print(zipped)
# Result: [(1, 'A'), (2, 'B'), (3, 'C')]