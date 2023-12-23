import spacy
import pandas as pd
from scipy import spatial


def space(token):
    return token.text, token.pos_, token.morph, token.dep_


def analysis(text):
    nlp = spacy.load('ru_core_news_sm')

    text = nlp(text)
    words = {
        'text': [],
        'pos': [],
        'morph': [],
        'dep': [],
    }

    for token in text:
        form, pos, morph, dep = space(token)
        words['text'].append(form)
        words['pos'].append(pos)
        words['morph'].append(morph)
        words['dep'].append(dep)

    data_words = pd.DataFrame(words)

    graph = data_words["pos"].value_counts().plot.bar(color='#182D09')
    # https://stackoverflow.com/questions/19555525/saving-plots-axessubplot-generated-from-python-pandas-with-matplotlibs-savefi
    fig = graph.get_figure()
    fig.savefig("output.png")

    return df_to_dict(data_words)


def df_to_dict(df):
    res = {'key': []}
    for i in df.index:
        line = ''
        line = line + str(df['text'][i]) + (20 - len(df['text'][i])) * " "
        line = line + str(df['lemma'][i]) + (20 - len(df['lemma'][i])) * " "
        line = line + str(df['pos'][i]) + (10 - len(df['pos'][i])) * " "
        line = line + str(df['dep'][i]) + (10 - len(df['dep'][i])) * " "
        line = line + str(df['vector'][i])[:36] + '...'
        res['key'].append(line)
    return res
