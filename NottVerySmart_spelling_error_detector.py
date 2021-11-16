import re
from collections import Counter
import string


# reference from post by Peter Norvig, Feb 2007 to August 2016, http://norvig.com/spell-correct.html
def words(text):
    return re.findall(r'\w+', string.capwords(text.lower()))  # return a list of strings matching the whole pattern


word_dict = Counter(words(open('NottVerySmart_spelling.txt').read()))  # count hashable objects, store objects as keys and counts as values
word_list = words(open('NottVerySmart_spelling.txt').read())


def probability(word, word_num=sum(word_dict.values())):
    return word_dict[word] / word_num  # probability of word


def correction(word):
    return max(candidates(word), key=probability)  # highest possibility of spelling correction for word


def candidates(word):
    return known([word]) or known(edits(word)) or [word]  # return possible spelling corrections for word


def known(words):
    return set(w for w in words if w in word_dict)  # create set for words present in word_dict


def edits(word):
    # edits that are one edit away from word
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits if b for c in letters]
    inserts = [a + c + b for a, b in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)









