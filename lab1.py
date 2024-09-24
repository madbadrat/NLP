import nltk
from nltk import sent_tokenize, word_tokenize

import pymorphy3

nltk.download('punkt')
m = pymorphy3.MorphAnalyzer()

with open('Malavita.txt', 'r', encoding='utf8') as file:
    text = file.read()

print(text)

sent = sent_tokenize(text)
for i in range(len(sent)):
    print(sent[i] + "\n")

for i in range(len(sent)):
    words = word_tokenize(sent[i])
    print(words)

for i in range(len(sent)):
    words = word_tokenize(sent[i])
    for j in range(len(words) - 1):
        currentWord = m.parse(words[j])[0]
        nextWord = m.parse(words[j + 1])[0]

        if (currentWord.tag.POS == "NOUN" and nextWord.tag.POS == "ADJF") or (
                currentWord.tag.POS == "ADJF" and nextWord.tag.POS == "NOUN"):
            if currentWord.tag.gender == nextWord.tag.gender:
                if currentWord.tag.number == nextWord.tag.number:
                    if currentWord.tag.case == nextWord.tag.case:
                        print(currentWord.normal_form + " " + nextWord.normal_form)