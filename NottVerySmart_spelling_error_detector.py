import re
from collections import Counter
import string


def words(text):
    return re.findall(r'\w+', string.capwords(text.lower()))


word_dict = Counter(words(open('NottVerySmart_spelling.txt').read()))
word_list = words(open('NottVerySmart_spelling.txt').read())


def probability(word, word_num=sum(word_dict.values())):
    return word_dict[word] / word_num


def correction(word):
    return max(candidates(word), key=probability)


def candidates(word):
    return known([word]) or known(edits(word)) or [word]


def known(words):
    return set(w for w in words if w in word_dict)


def edits(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)









