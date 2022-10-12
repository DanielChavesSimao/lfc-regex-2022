# a) Contabilizar o número países diferentes que aparecem no banco de dados, dados os emails que
# aparecem nas mensagens
import pandas as pd
import ast
from dani_utils import find

def preprocess():
    respostas = find('country')
    df = pd.DataFrame(data=respostas)
    df.to_csv('countries.csv',sep=';',index=False)

def run():
    df = pd.read_csv('countries.csv',sep=';')
    df = df.apply(lambda x: {"found": ast.literal_eval(x[0])},1,result_type='expand').explode('found').dropna().drop_duplicates().reset_index(drop=True)
    print(df)
    df.head(10).to_csv('resposta_a.csv',sep=';',index=False)

if __name__=='__main__':
    pass