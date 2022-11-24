#!/usr/bin/python

def get_sentiment(text_results, pos, neg):
    print(text_results)
    positive_feeling = []
    negative_feeling =[]
    for token in text_results:
        #print(token.text, token.pos_, token.dep_, token.tag_, token.morph)
        if token.text in pos['Word'].values:
            print(f'{token.text} is positive: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
            f'the morphology is {token.morph}')
            positive_feeling.append(token)
        elif token.text in neg['Word'].values:
            print(f'{token.text} is negative: and contains a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
            f'the morphology is {token.morph}')
            negative_feeling.append(token)
        else:
            continue     
    if len(positive_feeling) > len(negative_feeling):
        print('The sentence contains a Positive feeling')
    elif len(positive_feeling) < len(negative_feeling):
        print('The sentence contains a Negative feeling')
    else:
        'Job done'