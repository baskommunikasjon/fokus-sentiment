#!/usr/bin/python

def get_sentiment(text_results, pos, neg):
    print(text_results)
    for token in text_results:
        #print(token.text, token.pos_, token.dep_, token.tag_, token.morph)
        if token.text in pos['Word'].values:
            print(f'{token.text} is positive: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
            f'the morphology is {token.morph}')
            print('The sentence contains a Positive feeling')
        elif token.text in neg['Word'].values:
            print(f'{token.text} is negative: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
            f'the morphology is {token.morph}')
            print('The sentence contains a Negative feeling')
        else:
            continue     