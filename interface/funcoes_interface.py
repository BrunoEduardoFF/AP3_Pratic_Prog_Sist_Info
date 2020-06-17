#O objetivo deste módulo é conter todas as funções que envolvem a interface o jogo.
from auxiliar import funcoes_auxiliares

def cabecalho_destacado(texto,tamanho_linha,caractere_interface):
    """esta função destaca a string passada no parâmetro 'texto', utilizando-se de
    3 linhas, com tamanho de caracteres igual ao parâmetro 'tamanho_linha',
     sendo as linhas 1 e 3 preenchidas com o caractere especial passado no
     parâmetro 'caractere_interface' """
    print(caractere_interface * tamanho_linha)
    print(f'{texto:{caractere_interface}^{tamanho_linha}}')
    print(caractere_interface * tamanho_linha)

def desenha_forca(x=0):
    #representação visual da forca.
    print('----------')
    print('|        |')
    if x==0:
        print('|        ')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|')
    elif x==1:
        print('|        O')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|')
    elif x == 2:
        print('|        O')
        print('|        |')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|')
    elif x == 3:
        print('|        O')
        print('|       -|')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|')
    elif x == 4:
        print('|        O')
        print('|       -|-')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|')
    elif x == 5:
        print('|        O')
        print('|       -|-')
        print('|       / ')
        print('|        ')
        print('|        ')
        print('|')
    elif x == 6:
        print('|        O')
        print('|       -|-')
        print("|      / '\'")
        print('|        ')
        print('| Você foi enforcado! Tente novamente!')
        print('|')

def interface_menu_principal(nome_jogo,lista_opcoes):
    """esta função gera a interface para o menu principal do jogo, onde o parâmetro
    'nome_jogo' será destacado (vide cabecalho_destacado), e as opções serão apresentadas
    com base na lista passada através do parâmetro 'Lista_opcoes'.
     Ao fim, retorna o número inteiro referente à opção escolhida. """
    cabecalho_destacado(nome_jogo,50,'*')
    for indice,opcao in enumerate(lista_opcoes):
        print(f'{indice}. {opcao}')
    numero = funcoes_auxiliares.ler_inteiro('\nInsira a opção desejada: ')
    return numero

def situacao_palavra_secreta(letras_acertadas):
    """esta função imprime as letras acertadas até o momento, bem como as posições
    ainda não acertadas pelo jogador."""
    print('Palavra secreta: ', end=' ')
    for letra in letras_acertadas:
        print(letra, end=' ')
    print()

def imprime_letras_erradas(letras_erradas):
    """esta função imprime as letras erradas pelo jogador até o momento."""
    if (len(letras_erradas) > 0):
        print('Palpites errados: ', end='')
        for letra in letras_erradas:
            print(letra,end = ' ')

def mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_derrota(palavra_secreta):
    print("Você perdeu!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

