from collections import Counter


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

print(most_repeating_word(WORDS))


print('-'*100)
#Instead of finding the word with the greatest number of repeated letters, find the word with the greatest number of repeated vowels.


def most_repeting_vowel_count(word):
    vowel_in_word = ''

    for one_char in word.lower():
        if one_char in 'aeiou':
            vowel_in_word += one_char

    return Counter(vowel_in_word).most_common(1)[0][1]

def most_repeated_word(words):
    return max(words, key=most_repeting_vowel_count)

WORDS2 = ['this', 'is', 'an', 'elementary', 'test', 'example','aaabhilash']

print(most_repeating_word(WORDS2))
