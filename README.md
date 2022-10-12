# How to use

Extrair o dataset para o diretorio maildir na raiz do projeto

```
python main.py [option] letra_do_ex
```
|opcao|descricao|
|----|----|
|--preprocess ou -p| Salva um dataframe com os achados do regex em um arquivo txt ou csv|
|--run ou -r| Le os arquivos e retorna a resposta esperada|

Ex: 

```
python main.py -r f
```
Se nenhuma opcao for escolhida o algoritmo rodara o preprocessamento e a execucao em seguida.