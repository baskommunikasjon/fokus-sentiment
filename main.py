#! /usr/bin/python

import spacy
import numpy as np
import pandas as pd
from data_processing.get_labels import get_positive_and_negative_words
from data_processing.get_message import get_sentiment
from data_processing.save_excel import save_excel
# Load text
nlp = spacy.load("nb_core_news_sm")
'''
This is an nlp that separates the different parts of a sentence
'''

text_results = nlp('Frem til tirsdag kveld var Bruno Fernandes'
                   ' og Cristiano Ronaldo både lagkamerater for Portugal og'
                   ' Manchester United, men da kom beskjeden om'
                   ' at Ronaldo var ferdig for klubblaget.')  # nyhet1

text_results1 = nlp('Barentssekretariatet har vært til stede'
                    ' i de russiske byene Arkhangelsk, Murmansk og Narjan-Mar'
                    ', men driften ved kontorene vil bli avviklet med virkning '
                    'fra 1. februar neste år, skriver de på sine nettsider.'
                    'Det betyr at alle ansatte i Russland blir sagt opp.'
                    'Sekretariatet tilrettelegger de norsk-russiske'
                    ' samarbeidsprosjektene i norsk og russisk del av Barentsregionen.'
                    'Det er eid av Nordland og Troms og Finnmark fylkeskommuner,'
                    ' og fordeler midler til mellom 200 og 300 prosjekter hvert år.'
                    '– Vi har en gjeng med svært dyktige kolleger på våre kontorer i Russland.'
                    ' Det er trist at vi har havnet i den situasjonen vi er i nå,'
                    ' sier daglig leder Lars Georg Fordal i Barentssekretariatet.'
                    'Avgjørelsen kommer som en konsekvens av de utfordringene'
                    ' Russlands krig mot Ukraina har skapt for Barentssamarbeidet.')
# nyhet2

# Get positive and negative lists

pos, neg = get_positive_and_negative_words()

# Get sentiment of each text

positive_results, negative_results = get_sentiment(text_results, pos, neg)
print('First text is done\n')
print('\n')
positive_results1, negative_results1 = get_sentiment(text_results1, pos, neg)

# Save excel files

save_excel(positive_results, negative_results,
           'Result 1',
           'Positive results', 'Negative results')
save_excel(positive_results1, negative_results1,
           'Result 2',
           'Positive results', 'Negative results')
