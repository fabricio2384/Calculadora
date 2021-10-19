import os                       #Importa a biblioteca do sistema
clear = lambda: os.system('cls')#Função com comando para limpar a tela do prompt
clear()

def textoInicial():             #Função para imprimir na tela os dados necessarios para a operação
    print('--------------------------Calculadora v1.0 --------------------------\n')
    print('-----------------------------------------')
    print('Selecione o número da operação desejada  |')
    print('1 - Soma                                 |')
    print('2 - Subtração                            |')
    print('3 - Multiplicação                        |')
    print('4 - Divisão                              |')
    print('Digite exite para sair                   |')
    print('-----------------------------------------\n')
#-----------------------------------------------------------
#Funções de operação
soma = lambda: (num1 + num2)
subtrai = lambda: (num1 - num2)
multiplca =  lambda: (num1 * num2)
dividi = lambda: (num1 / num2)
#-----------------------------------------------------------

textoInicial()
operacao = (input('Digite uma opção (1/2/3/4): ')) # Valores de entrada para cada operação

while operacao != 'exit':                          # Chamada para sair do programa

    operacao = int(operacao)
    if operacao > 4 or operacao == 0:              # Verificação se as opções estão corretas 1,2,3,4
        print('Opção invalida')
    else:
        num1 = int(input('Digite o primeiro número: ')) #Entrada do primeiro valor da operação
        num2 = int(input('Digite o segundo número: '))  #Entrada do segundo valor da opeeração
        if operacao == 1:                                    # 1 Soma
             print('Resultado:',num1,'+',num2,'=',soma())      # 2 Subtração
        elif operacao == 2:
             print('Resultado:', num1, '-', num2, '=', subtrai()) # 3 Multiplição
        elif operacao == 3:
             print('Resultado:', num1, 'x', num2, '=', multiplca())
        elif operacao == 4:                                  # 4 Divisão
             print('Resultado:', num1, '/', num2, '=', dividi())
    input("\nPrecione Enter para continuar: ")               # Stop para visualizar o valor do resultado, pressionando Enterpara Sair
    clear()                                                  # Comando para limpar o prompt
    textoInicial()
    operacao = (input('Digite uma opção (1/2/3/4): '))       # Nova chamada para resolver operações




