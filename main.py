#! /usr/bin/python

import spacy 
import numpy as np

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