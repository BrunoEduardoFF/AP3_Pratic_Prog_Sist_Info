#Este módulo contém algumas funções de utilidade auxiliar, utilizadas no código principal.

def ler_inteiro(msg):
    """ esta função garante que o input do usuário será um número inteiro.
    No parâmetro 'msg', deverá ser inserida a mensagem de input para o usuário."""
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário não digitou o número. \033[m')
            return 0
        else:
            return numero

def checar_nome(nome_jogador, nome_arquivo="jogadores.txt"):
    """esta função irá carregar todos os dados do arquivo 'jogadores.txt' em listas,
    e tentará localizar o nome do jogador. Caso localize, retornará um objeto da classe Jogador,
    contendo nome e pontuação do jogador. """
    arquivo = open(nome_arquivo,'r')
    todos_jogadores = list()
    for linha in arquivo:
        atributos_jogador = linha.split(';')
        todos_jogadores.append(atributos_jogador)
    arquivo.close()
    for jogador in todos_jogadores:
        """caso o nome do jogador seja localizado, a classe será carregada com seu histórico
        de pontos anterior, cadastrado no arquivo 'jogadores.txt'. """
        if nome_jogador.upper().strip() in jogador:
            print(f'Bem vindo de volta, {nome_jogador}!')
            jogador_ativo = Jogador(jogador[0],jogador[1],jogador[2],jogador[3])
            return jogador_ativo
    """este bloco somente será executado caso o nome do jogador não seja localizado,
    carregando a classe com pontuação zerada."""
    print(f'Bem vindo {nome_jogador}! Primeira vez jogando!')
    jogador_ativo = Jogador(nome_jogador,0,0,0)
    return jogador_ativo

class Jogador(object):
    """esta classe armazenará os dados de cada jogador em seus atributos.
    também contém as regras para adicionar vitórias, derrotas e partidas jogadas ao seu placar
    individual."""
    def __init__(self, nome, partidas_jogadas=0,partidas_vencidas=0,partidas_perdidas=0):
        self.nome = nome
        self.partidas_jogadas = int(partidas_jogadas)
        self.partidas_vencidas = int(partidas_vencidas)
        self.partidas_perdidas = int(partidas_perdidas)

    def adiciona_vitoria(self):
        self.partidas_jogadas +=1
        self.partidas_vencidas +=1

    def adiciona_derrota(self):
        self.partidas_jogadas +=1
        self.partidas_perdidas +=1

    def exibe_dados(self):
        print('*' * 30)
        print(f'Jogador: {self.nome}')
        print(f'Partidas jogadas: {self.partidas_jogadas}')
        print(f'Vitórias: {self.partidas_vencidas}')
        print(f'Derrotas: {self.partidas_perdidas}')
        print('*' * 30)

def gravar_placar(jogador_ativo, nome_arquivo="jogadores.txt"):
    """esta função se encarrega de sobrescrever o arquivo 'jogadores.txt' com
    os novos dados (vitoria ou derrota do jogador).
    Caso o jogador já exista no arquivo, a posição original no arquivo será
    respeitada, alterando a pontuação para a atual (após jogar). Caso seja a
    primeira vez do jogador, irá criar, ao final do arquivo, uma nova linha com
    seus dados."""
    todas_linhas = carregar_lista_com_arquivo(nome_arquivo)

    jogador_esta_na_lista = False
    for indice, jogador in enumerate(todas_linhas):
        if jogador[0] == jogador_ativo.nome:
            todas_linhas[indice][0] = jogador_ativo.nome
            todas_linhas[indice][1] = jogador_ativo.partidas_jogadas
            todas_linhas[indice][2] = jogador_ativo.partidas_vencidas
            todas_linhas[indice][3] = jogador_ativo.partidas_perdidas
            jogador_esta_na_lista = True
            break
    if(not jogador_esta_na_lista):
        nova_linha = []
        nova_linha.append(jogador_ativo.nome)
        nova_linha.append(jogador_ativo.partidas_jogadas)
        nova_linha.append(jogador_ativo.partidas_vencidas)
        nova_linha.append(jogador_ativo.partidas_perdidas)
        todas_linhas.append(nova_linha)

    arquivo = open(nome_arquivo, 'w')
    for linha in todas_linhas:
        for indice, dado in enumerate(linha):
            if indice == 3:
                arquivo.write(str(dado))
            else:
                arquivo.write(str(dado) + ';')
        arquivo.write('\n')
    arquivo.close()

def carregar_lista_com_arquivo(nome_arquivo):
    """esta função é utilizada para carregar uma lista com todas as informações
    do arquivo 'nome_arquivo', separando os dados em subslistas., ao final,
    retorna a lista com todos os dados."""
    arquivo = open(nome_arquivo, 'r')
    todas_linhas = []

    for linha in arquivo:
        dados_linha = linha.split(';')
        for indice, dado in enumerate(dados_linha):
            dados_linha[indice] = dado.strip()
        todas_linhas.append(dados_linha)
    arquivo.close()
    return todas_linhas