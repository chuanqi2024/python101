
from string import punctuation
from typing import Counter


def load_text(input_file):
    with open(input_file, "r", encoding = "utf-8") as file:
        text = file.read()
    return text


def clean_text(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)

