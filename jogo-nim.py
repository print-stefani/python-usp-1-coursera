
def computador_escolhe_jogada(n, m):
    c_remove = 1
    while c_remove != m:
        if (n - c_remove) % (m + 1) == 0:
            return c_remove
        else:
            c_remove += 1
    return c_remove


def usuario_escolhe_jogada(n, m):
    jogada_val = True
    
    while jogada_val:
        j_remove = int(input('Quantas peças você vai tirar? '))
        if j_remove > m or j_remove < 1:
            print('\n<<<< Oops! Jogada inválida! Tente de novo. >>>>\n')
        else:
            jogada_val = False
    return j_remove


def partida():
    n = int(input('Quantas peças:  '))
    m = int(input('Limite de peças por jogada: '))
    c_vez = False
    
    if n % (m + 1) == 0:
        print('\nVoce começa!\n')
    else:
        print('\nComputador começa!')
        c_vez = True
        
    while n > 0:
        if c_vez:
            c_remove = computador_escolhe_jogada(n, m)
            n = n - c_remove
            if c_remove == 1:
                print('\nO computador tirou uma peça.')
            else:
                print('\nO computador tirou', c_remove, 'peças.')
            c_vez = False
        else:
            j_remove = usuario_escolhe_jogada(n, m)
            n = n - j_remove
            
            if j_remove == 1:
                print('\nVocê tirou uma peça.')
            else:
                print('\nVocê tirou', j_remove, 'peças.')
            c_vez = True
        if n == 1:
            print('Restam apenas uma peça no tabuleiro.')
        else:
            if n != 0:
                print ("Agora restam %.0f peças no tabuleiro.\n" % (n))
                
    print ("\n|||||||||||||||||||||||||||||||||||||||")            
    print('||\t\t\t\t     ||\n|| Fim do jogo! O computador ganhou! ||\n||\t\t\t\t     ||')
    print ("|||||||||||||||||||||||||||||||||||||||")            

def campeonato():
    rodada = 1
    
    while rodada <= 3:
        print ("\n||||||||||||||||||||||||||")
        print ("||\tRodada n° %2.0f \t||" % (rodada))
        print ("||||||||||||||||||||||||||\n")

        partida()
        rodada += 1
        
    print ("\n|||||||||||||||||||||||||||||||||||||||")            
    print('||\t\t\t\t     ||\n||         Fim do Campeonato!\t     ||\n||\t\t\t\t     ||')   
    print('||   Placar: Você 0 X 3 Computador   ||\n||\t\t\t\t     ||')
    print ("|||||||||||||||||||||||||||||||||||||||")     
    

# Início do jogo do NIM

def jogo_nim ():
    
    print('Bem-vindo ao jogo do NIM!\nEscolha um numero:\n')
    part = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n'))

    while part != 1 and part != 2:
        print('\nOpção invalida! Tente de novo...\n')
        part = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n'))
    
    if part == 1:
        print()
        partida()
    else:
        print('\nVoce escolheu um campeonato!')
        campeonato()

