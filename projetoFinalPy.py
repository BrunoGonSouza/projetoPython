''' CST em Análise e desenvolvimento de sistemas (ADS)
    Campus: Guarulhos
    Turma: 1k
    Grupo: Bruno (RGM:29078989)
           Fernando (RGM: 29220041)
           Sabrina (RGM: 29983240)

    Entrega do projeto: 16/05/2022
    Disciplinas: Organização e arquitetura de computadores (Carlos Alexandre) e Programação de computadores (Vinicius heltai)
    Proposta do projeto: O projeto interdisciplinar deste semestre tem como objetivo promover a integração das disciplinas de Organização e Arquitetura
    de Computadores e Programação de Computadores e consiste na construção de um software utilizando-se da linguagem de programação Python, que permita
    a realização de operações que envolvam Sistemas de Numeração. Apropriando-se da tecnologia descrita acima, cada grupo deverá desenvolver um programa
    para resolver questões pertinentes a um problema específico a ser escolhido dentre as opções apresentadas abaixo:
    Opção 1: Conversão da base decimal para as bases binário, hexadecimal e octadecimal.
    Opção 2: Conversão das bases binário, hexadecimal e octadecimal para a base decimal.

    Opção escolhida: 1 (Conversão da base decimal para as bases binário, hexadecimal e octadecimal)'''

                                                                #Projeto Interdisciplinar

#entrada
print("       Software de conversão de base decimal")
print("                                            ")

while (True):
    numero = input("Digite um número em decimal para conversão (ex.: 423): ")
    if (numero.isalpha()):
        print("Proibido letras")
        break
    
    numero = int(numero)
    if numero < 1:
        print("Apenas números positivos ou acima de 0")
    else:
        print('''Opções de bases para conversão:
     1 = Converter para Binário
     2 = Converter para Octal
     3 = Converter para Hexadecimal''')
            
        tipoConversao = int(input("Escolha uma das opções acima para fazer a conversão (ex.: 1): "))
              
            
        if (tipoConversao == 0 or tipoConversao >= 4):
            print("Opção inválida, tente de novo")
            
        #Conversão de Binario        
        elif (tipoConversao == 1 and numero >= 0):
            
            binario = ''
            while numero > 0:
                resto = numero%2
                numero = int(numero/2)
                binario = binario + str(resto)
            binario = binario + ''
            print (f"O número em binario é {binario[-1::-1]}")
            
        #Conversão de Octal        
        elif (tipoConversao == 2 and numero == 0):
            print (f"O número em Octal é 0")
        elif (tipoConversao == 2 and numero >= 0):
            octal = ''
            while numero > 0:
                resto = numero%8
                numero = int(numero/8)
                octal = octal + str(resto)
            octal = octal + ''
            print (f"O número em octal é {octal[-1::-1]}")
            
        #Conversão de Hexadecimal    
        elif (tipoConversao == 3 and numero == 0):
            print (f"O número em Hexadecimal é 0")
        elif (numero > 0):
            hexa = ''
            dicionario = {0:'0', 1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
            while numero > 0:
                resto = numero%16
                numero = int(numero/16)
                hexa = dicionario[resto] + hexa
            print (f"O numero em hexadecimal é {hexa}")
            
        print("                                                              ")
        sair = input("Digite S para sair ou qualquer tecla para continuar ")
        if (sair == "S" or sair == "s"):
            break
        print("--------------------------------------------------------------")





    








