import a,b,c,d,f
import sys, getopt

files = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'f': f,
}

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],'pr', ['preprocess','run'])
        if len(args) == 0:
            raise getopt.GetoptError('Argumento para a escolha do exercicio faltando.\n python main.py [--options] file_name')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for o, a in opts:
        if o in ('-p', '--preprocess'):
            print(f'Preprocessando {args[0]})...')
            print('...pode demorar até algumas horas...')
            files[args[0]].preprocess()
            print(f'{args[0]}) preprocessado com sucesso!')
        elif o in ('-r', '--run'):
            print(f'Rodando {args[0]})...')
            files[args[0]].run()

    if len(opts)==0:
        print(f'Preprocessando {args[0]})...')
        print('...pode demorar até algumas horas...')
        files[args[0]].preprocess()
        print(f'Rodando {args[0]})...')
        files[args[0]].run()
    print('Encerrando.')

if __name__ == '__main__':
    main()