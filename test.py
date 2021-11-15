import re
from collections import Counter


def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('').read()))


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
print(correction(inp))

