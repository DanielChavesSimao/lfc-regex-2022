from re import findall, MULTILINE
import os
from tqdm import tqdm

def findDollarsInFile(path: str) -> dict:
    dolarRegex = r'(\$\d+(,?\d{3})*(\.\d\d)?)'
    return findRegexInFile(path, dolarRegex)

def findWwwsInFile(path: str) -> dict:
    wwwRegex = r'((https?:\/\/)?(www\.)[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))'
    return findRegexInFile(path, wwwRegex)

def findEmailsInFile(path: str) -> dict:
    emailRegex = r"([\w\-\.]+@([\w-]+\.)+[\w-]{2,4})"
    return findRegexInFile(path, emailRegex)

def findCountriesInFile(path: str) -> dict:
    with open('allcountries.txt','r') as f:
        countryRegex = '(' + r'|'.join(f.read().split('\n')) + ')'
    return findRegexInFile(path, countryRegex)

def findRegexInFile(path, regex)->dict:
    with open(path, 'r') as f:
        resposta = {
            "found": findall(regex, f.read(), MULTILINE),
            "file_name": path
        }
    return resposta

def find(what:str)->list:
    tipos = {
        'dollar': findDollarsInFile,
        'email': findEmailsInFile,
        'country': findCountriesInFile,
        'www': findWwwsInFile,
    }
    rootpath = os.path.join(os.getcwd(), 'maildir')
    respostas = list()
    count = 0
    for dirpath, dirname, filenames in tqdm(os.walk(rootpath)):
        count += len(filenames)
    for dirpath, dirname, filenames in tqdm(os.walk(rootpath),total=count,desc='progresso total'):
        for name in tqdm(filenames,leave=False,bar_format='{l_bar}{bar:75}|',desc='progresso do dir atual'):
            with open(os.path.join(dirpath, name), 'r') as f:
                respostas.append(tipos[what](os.path.join(dirpath, name)))
    return respostas

if __name__=='__main__':
    pass