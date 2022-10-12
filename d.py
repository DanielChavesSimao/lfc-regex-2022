# d) Contabilizar o número de endereços www que aparecem nas mensagens e listar os cinco mais 
# frequentes;
import pandas as pd
from dani_utils import find

def preprocess():
    respostas = find('www')

    df = pd.DataFrame(data=respostas).explode('found').reset_index(drop=True).dropna().apply(lambda x: {'www': x[0][0], 'file_name':x[1]}, axis=1, result_type='expand')
    
    df.to_csv('wwws.csv',sep=';',index=False)

def run():
    df = pd.read_csv('wwws.csv',sep=';')
    filteredDf = df.groupby(['www'])['www'].count().sort_values(ascending=False)
    print(filteredDf[:5])
    filteredDf[:5].to_csv('resposta_d.csv',sep=';',index=False)

if __name__ == '__main__':
    pass