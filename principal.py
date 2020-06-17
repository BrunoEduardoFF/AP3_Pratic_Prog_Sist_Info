from interface import funcoes_interface
from auxiliar import funcoes_auxiliares
from random import randrange
from time import sleep

def menu_principal():
   """esta função é a que inicializa o programa, gerando o menu principal e
    guardando as informações de quantas vezes o jogador venceu, perdeu, jogou, etc.
    De acordo com a escolha, diferentes funções serão chamadas."""
   lista_opcoes = ['Jogar','Placar','Sair']
   opcao = funcoes_interface.interface_menu_principal('     JOGO DA FORCA     ', lista_opcoes)
   if opcao == 0:
       opcao_jogar()
   elif opcao == 1:
       opcao_placar()
   else:
       print('Obrigado por jogar!')


def opcao_jogar():
    """esta função será executada quando o jogador escolher a opção "Jogar" no
    menu principal. Em sequência, perguntará o nome do jogador e ativará a função
    que verifica se o jogador já jogou antes. Por fim, exibe os dados do jogador."""
    print('\n' * 30)
    nome_jogador = str(input('Insira o seu nome: ')).upper().strip()
    sleep(0.5)
    #jogador_ativo é um objeto da classe Jogador
    jogador_ativo = funcoes_auxiliares.checar_nome(nome_jogador)
    sleep(0.5)
    print()
    jogador_ativo.exibe_dados()
    input('Pressione ENTER para continuar...')
    jogo_da_forca(jogador_ativo)

def opcao_placar():
    """esta funcão se encarrega de exibir o placar atual, com base no arquivo 'jogadores.txt'"""
    print('\n'*30)
    funcoes_interface.cabecalho_destacado('    PLACAR    ', 50, 'X')
    todas_linhas = funcoes_auxiliares.carregar_lista_com_arquivo('jogadores.txt')
    print('---------------------------------------------')
    print('JOGADOR        PARTIDAS   VITORIAS   DERROTAS')
    print('---------------------------------------------')
    for linha in todas_linhas:
        print(f'{linha[0]:<15}{linha[1]:<11}{linha[2]:<11}{linha[3]:<8}')
    print()
    input('Pressione ENTER para continuar...')
    print('\n'*30)
    menu_principal()


def jogo_da_forca(jogador_ativo):
    """esta é a função principal, onde será rodada uma partida de jogo.
    Usa como parâmetro um objeto da classe Jogador"""
    venceu = False
    perdeu = False
    erros = 0
    palavra_secreta = escolher_palavra_secreta('palavras.txt')
    letras_erradas = list()

    #o comando abaixo separa a palavra secreta em uma lista: palavra[0] e dica [1].
    palavra_secreta = palavra_secreta.split(';')

    """#inicializa a palavra secreta em uma variável do tipo lista, para que se
    possa alterar seus caracteres individualmente. O caractere '_' servirá para
    que o jogador saiba quantas letras a palavra secreta possui."""
    letras_acertadas = ['_' for letra in palavra_secreta[0]]

    funcoes_interface.desenha_forca(erros)

    while(not perdeu and not venceu):
    #laço principal do jogo, enquanto não perder nem vencer haverá iteração.
        funcoes_interface.imprime_letras_erradas(letras_erradas)
        print('\n')
        funcoes_interface.situacao_palavra_secreta(letras_acertadas)
        print(palavra_secreta[1])
        print()

        palpite = obter_palpite(input('Insira o seu palpite: '))

        if palpite in palavra_secreta[0]:
            print('Você acertou!')
            sleep(0.3)
            """este bloco checa a presença da letra palpitada na palavra secreta,
            caso encontre, insere o palpite na posição correspondente"""
            for indice, letra in enumerate(palavra_secreta[0]):
                if palpite == letra:
                    letras_acertadas[indice] = palpite
        else:
            #em caso de erro, a forca será desenhada progressivamente mais próxima da derrota.
            erros+=1
            print('Você errou!')
            sleep(0.3)
            funcoes_interface.desenha_forca(erros)
            letras_erradas.append(palpite)

        #checagem lógica de vitória ou derrota:
        venceu = '_' not in letras_acertadas
        perdeu = erros == 6

        """os blocos abaixo geram a mensagem de vitoria ou derrota e modificam
        a pontuação do jogador (ver classe Jogador)."""
        if(venceu):
            sleep(1)
            funcoes_interface.mensagem_vitoria()
            jogador_ativo.adiciona_vitoria()
            break
        if(perdeu):
            sleep(1)
            funcoes_interface.mensagem_derrota(palavra_secreta[0])
            jogador_ativo.adiciona_derrota()
            break
    print()
    input('Pressione ENTER para continuar...')

    # ver função utilizada abaixo para detalhes do funcionamento de gravação da pontuação.
    funcoes_auxiliares.gravar_placar(jogador_ativo)
    menu_principal()


def escolher_palavra_secreta(nome_arquivo):
    """passa o conteúdo das linhas do arquivo passado no parâmetro 'nome_arquivo'
    para a lista chamada 'lista_palavras'. Após, escolhe aleatóriamente um dos itens da lista
    e retorna-o em caixa alta. """
    arquivo = open(nome_arquivo, 'r')
    lista_palavras = [linha.strip() for linha in arquivo] #o método strip retira o newline '\n' da linha.
    arquivo.close()
    return lista_palavras[randrange(0,len(lista_palavras))].upper()

def obter_palpite(letra):
    """esta função é utilizada para obter o palpite do jogador, limpando espaços, tornando maiúscula e
    aceitando apenas a primeira letra digitada, caso digite mais de uma."""
    letra = letra.strip()
    if (len(letra)>1):
        letra = letra[0]
    letra = letra.upper()
    return letra

if (__name__=='__main__'):
    """uma vez que o jogo está dentro de uma função, esta checagem permite sua
    execução caso o arquivo 'principal.py' seja diretamente executado."""
    menu_principal()