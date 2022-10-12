# c) Localizar a mensagem que conta com o maior número de usuários (emails) diferentes;

import os, pandas as pd
from dani_utils import find
import ast

def preprocess():
    respostas = find('email')

    df = pd.DataFrame(data=respostas)
    df.to_csv('emails.csv',sep=';',index=False)

# bug
    # print(df)
    # print(df.dtypes)
    # df = df.explode('found')
    # print(df)
    # df = df.dropna()
    # print(df)
    # df = df.apply(lambda x: [x[0][0], x[1]], axis=1, result_type='broadcast')
    # print(df)

def run():
    df = pd.read_csv('emails.csv',sep=';')
    df = df.apply(lambda x: [ast.literal_eval(x[0]), x[1]],1,result_type='broadcast').explode('found')
    df.drop_duplicates(inplace=True)
    dfC = df.groupby(['file_name']).count().sort_values(by='found',ascending=False)
    # finalAnswer = dfC.loc[[dfC.idxmax()[0]]]
    print(dfC)
    dfC.head(10).to_csv('resposta_c.csv',index=False,sep=';')

if __name__ == '__main__':
    pass