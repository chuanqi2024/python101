from python101.pycounts import count_words
from collections import Counter

expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
 'the': 1, 'same': 1, 'thing': 1,
 'over': 2, 'and': 2, 'expecting': 1,
 'different': 1, 'results': 1})

actual = count_words("tests/einstein.txt")

assert actual == expected


