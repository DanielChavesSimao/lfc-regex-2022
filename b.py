# b) Determinar se existem ocorrências de valores de em dólares nas mensagens,  se aparecer 
# apresentar a mensagem como o maior valor;

import pandas as pd, re
from dani_utils import find

def preprocess():
    respostas = find('dollar')
    with open('dolares.csv', 'w') as f:
        for resposta in respostas:
            for dollarFound in resposta["found"]:
                f.write(dollarFound[0] + ';' + resposta["file_name"] + '\n')

def run():
    df = pd.read_csv('dolares.csv', sep=';')
    df = df.apply(lambda x: {'valor':float(re.sub(r'[^\d.]','',x[0])),'file':x[1]},axis=1,result_type='expand')
    df = df.sort_values(by='valor',ascending=False)
    print(df)
    df.head(10).to_csv('resposta_b.csv',sep=';',index=False)

if __name__ == '__main__':
    pass