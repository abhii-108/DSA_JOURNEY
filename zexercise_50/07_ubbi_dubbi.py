import re, string
def ubbi_dubbi(word):
    output = []

    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    return ''.join(output)

print(ubbi_dubbi('abhilash'))

def ubbi_dubbi_translate(word):
    ## another way of doing 
    pattern = '[aeiou]'
    replacement = 'ub'

    return  re.sub(pattern, replacement, word, flags=re.IGNORECASE)

print(ubbi_dubbi_translate('abhilash'))

def ubbi_dubbi_caps(word):
    output = []

    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    if word[0] in string.ascii_uppercase:
        output[0] = output[0].capitalize()
    
    return ''.join(output)


#print(ubbi_dubbi_caps(input('Enter some word to change..!')))



def remove_authors_names(text, names):

    output = text 

    for one_name in names:
        output = output.replace(one_name, '_'*len(one_name))

    return output


print(remove_authors_names('We got speaker ronald in house',['ronald']))