#!/usr/bin/python

# Import packages
import pandas as pd

# Functions


def get_sentiment(text_results, pos, neg):
    print(text_results)
    positive_feeling = []
    negative_feeling = []
    for token in text_results:
        #print(token.text, token.pos_, token.dep_, token.tag_, token.morph)
        if token.text in pos['Word'].values:
            print(f'{token.text} is positive: and contains'
                  f' a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
                  f'the morphology is {token.morph}')
            df_token = pd.DataFrame(
                {'Word': token.text,
                 'Part of speech tag - coarsed grained': token.pos_,
                 'Dependency label': token.dep_,
                 'Part og speech tag - fine grained': token.tag_,
                 'Morphology': token.morph})
            positive_feeling.append(df_token)
        elif token.text in neg['Word'].values:
            print(f'{token.text} is negative: and contains'
                  f' a {token.pos_, token.dep_} tagged as {token.tag_}, and \n'
                  f'the morphology is {token.morph}')
            df_token = pd.DataFrame(
                {'Word': token.text,
                 'Part of speech tag - coarsed grained': token.pos_,
                 'Dependency label': token.dep_,
                 'Part og speech tag - fine grained': token.tag_,
                 'Morphology': token.morph})
            negative_feeling.append(df_token)
        else:
            continue
    if len(positive_feeling) > len(negative_feeling):
        print('The sentence contains a Positive feeling')
    elif len(positive_feeling) < len(negative_feeling):
        print('The sentence contains a Negative feeling')
    else:
        'Recognition done'
    try:
        positive_feelings_full = pd.concat(positive_feeling)
        negative_feelings_full = pd.concat(negative_feeling)
    except Exception:
        positive_feelings_full = negative_feeling
        negative_feelings_full = positive_feeling
    print(positive_feelings_full)
    print(negative_feelings_full)
    return positive_feelings_full, negative_feelings_full