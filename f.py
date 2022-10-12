# f) compare os tempos de processamento médios de regex e Boyer-Moore para localizar a palavra 
# price

import os, re
from timeit import timeit
import boyermoore

rootpath = os.path.join(os.getcwd(), 'maildir')
def regexFindPrice():
    for dirpath, dirname, filenames in os.walk(rootpath):
        for name in filenames:
            with open(os.path.join(dirpath, name), 'r') as f:
                price = re.search('price', f.read())
                if price:
                    return 1
    return 0

def boyermooreFindPrice():
    for dirpath, dirname, filenames in os.walk(rootpath):
        for name in filenames:
            with open(os.path.join(dirpath, name), 'r') as f:
                price = boyermoore.search('price', f.read())
                if price:
                    return 1
    return 0
def preprocess():
    setup = """import os, re, boyermoore
from f import regexFindPrice, boyermooreFindPrice
rootpath = os.path.join(os.getcwd(), 'maildir')"""

    tempoR = timeit(setup = setup, stmt = 'regexFindPrice()')
    print(f'Regex: {tempoR:.4f}s')

    tempoB = timeit(setup = setup, stmt = 'boyermooreFindPrice()')
    print(f'Boyermoore: {tempoB:.4f}s')

    with open('f.txt', 'w') as f:
        f.write(f'Regex: {tempoR:.4f}s\nBoyermoore: {tempoB:.4f}s')

def run():    
    with open('f.txt', 'r') as f:
        print(f.read())



if __name__ == '__main__':
    pass