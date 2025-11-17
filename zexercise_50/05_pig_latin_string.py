import string
def pig_latin(word):

    if word[0] in 'aeiou':
        return f'{word}way'
    
    return f'{word[1:]}{word[0]}ay'


print(pig_latin('python'))


def pig_latin_upper(word):
    if word[0].lower() in 'aeiou':
        output= f'{word}way'
    
    else:
        output= f'{word[1:]}{word[0]}ay'
    
    if word[0] in string.ascii_uppercase:
        output = output.capitalize()

    return output

print(pig_latin_upper('Python'))
print(pig_latin_upper('Abhilash'))


def pig_latin_punctuated(word):

    punctuation = ''

    if word[-1] in '.!?':
        punctuation = word[-1]
        word  = word[:-1]
        op = pig_latin_upper(word)
        #return f'{op}{punctuation}' ## we can also write op+punctuation
        return op+punctuation
    else:
        return pig_latin_upper(word)
    
print(pig_latin_punctuated('Abhilash!'))
print(pig_latin_punctuated('Python is good ?'))


    