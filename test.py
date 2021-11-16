import re
from collections import Counter
import NottVerySmart_functions as f
import string


def words(text):
    return re.findall(r'\w+', string.capwords(text.lower()))


WORDS = Counter(words(open('test.txt').read()))
word_list = words(open('test.txt').read())


def probability(word, n=sum(WORDS.values())):
    return WORDS[word] / n


def correction(word):
    return max(candidates(word), key=probability)


def candidates(word):
    return (known([word]) or known(edits1(word)) or [word])


def known(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


inp = input("You: ")
request_list = f.clean_input(inp)

for request in request_list:
    if correction(request) != request:
        for wl in word_list:
            if correction(request) == wl:
                print("Bots: Instead of " + request + " did you mean " + wl + "?")



