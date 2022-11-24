#! /usr/bin/python

import spacy 
import numpy as np
import pandas as pd
from data_processing.get_labels import get_positive_and_negative_words

# Load text
nlp = spacy.load("nb_core_news_sm")
'''
This is an nlp that separates the different parts of a sentence
'''

text_results = nlp('Frem til tirsdag kveld var Bruno Fernandes'
' og Cristiano Ronaldo både lagkamerater for Portugal og'
' Manchester United, men da kom beskjeden om'
' at Ronaldo var ferdig for klubblaget.')
print(text_results)
for token in text_results:
    print(token.text, token.pos_, token.dep_, token.tag_, token.morph)

pos, neg = get_positive_and_negative_words()

for token in text_results:
    #print(token.text, token.pos_, token.dep_, token.tag_, token.morph)
    if token.text in pos['Word'].values:
        print(f'{token.text} is positive: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and /n'
        f'the morphology is{token.morph}')
    elif token.text in neg['Word'].values:
        print(f'{token.text} is negative: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and /n'
        f'the morphology is{token.morph}')
    else:
        continue     