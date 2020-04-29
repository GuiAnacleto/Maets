#auto-py-to-exe

#BABRIOGECAS
import os
import subprocess
import time
import os
import sys


#==============================================FUNC==============================================
def Menu():
    print("=======================MENU========================\n")
    print("1 - Lista de Todos os Programas Cadastrados\n")
    print("2 - Executar Programa\n")
    print("3 - Cadastrar Programa\n")    
    print("4 - Limpa Tela\n")
    print("0 - Sair\n")    

    OP = input("Insira a opção desejada: ")
    MenuPrincipal(OP)

def Menu_Four():
    os.system('cls' if os.name == 'nt' else 'clear')
    Menu()    

def Menu_One():
    arquivo = open('DATA.txt', 'r')
    linha = arquivo.readline()
    print(linha)
    i = 1 
    while linha != "": 
        linha = arquivo.readline()
        if linha == "":
            Menu()
        
        print(linha)
        i = i + 1
    arquivo.close()
    Menu()

def Menu_Two():
    cod_program = input("Digite o codigo do programa que deseja abrir: ")
    caminho = RetCam(cod_program)
    caminho = caminho.replace("\\\\","/") 
    caminho = caminho.replace("\\","/")     
    caminho = caminho.replace("\n","")       
    os.startfile(caminho)
    
    Menu()

def Menu_Three():    
    Nome = input("Insira o Nome do Programa: ")
    Caminho = input("Insira o Caminho do seu programa: ")
    Desc = input("Insira uma Descrição:" )
    Cod = str(RetCod())

    print("\n\nOs Dados do seu programa são:\n")
    print("=================================================\n")
    print("\nCodigo: " + Cod)
    print("\nNome: " + Nome)
    print("\nCaminho: " + Caminho)
    print("\nDescrição: " + Desc)
    print("\n=================================================\n")
    opcao = input("Deseja Salvar?(S/N): ")

    if opcao == "N" or opcao == "n":
        print("\n")
        Menu()
    elif opcao == "S" or opcao == "s":
        # Abra o arquivo (leitura)
        arquivo = open('DATA.txt', 'r')
        conteudo = arquivo.readlines()

        if Cod == 1:
            conteudo.append("-----------------------------------------------------------\n" + "Codigo: " + Cod + "\n" + "Nome: "+Nome+"\n"+"Caminho: "+Caminho+"\n"+"Descrição: "+ Desc + "\n-----------------------------------------------------------\n")
        # insira seu conteúdo        
        conteudo.append("Codigo: " + Cod + "\n" + "Nome: "+Nome+"\n"+"Caminho: "+Caminho+"\n"+"Descrição: "+ Desc + "\n-----------------------------------------------------------\n")

        # Abre novamente o arquivo (escrita)
        # e escreva o conteúdo criado anteriormente nele.
        arquivo = open('DATA.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
        Menu()

def Menu_Five():
    SenhaFormat = input("Digite a Senha para formatar o programa: ")

    if SenhaFormat == "987323219":
        arquivo = open('DATA.txt', 'w')
        arquivo.close()

        arquivo = open('CONT.txt', 'w')
        arquivo.close()

        arquivo = open('CONT.txt', 'w')
        arquivo.write("0")
        arquivo.close()
        print("Arquivos Formatos com Sucesso!!\n\n")
        
        Menu()
    

def MenuPrincipal(argument):
    if argument == "2":
        Menu_Two()
    elif argument == "3":
        Menu_Three()   
    elif argument == "5":
        Menu_Five()
    elif argument == "1":
        print("-----------------------------------------------------------\n")
        Menu_One()
    elif argument == "4":
        Menu_Four()  
    elif argument == "0":
        sys.exit()             
        
        

def Vetoriza(string): #Arruma Caminho do Programa
    new_string = []
    for char in range(len(string)):
       new_string.append(string[char])
       if new_string == "\\":
        new_string.append(string["/"])
    return ''.join(new_string)

def RetCodClean(string): #Retorna o Codigo do Programa Limpo
    new_string = []
    cont = 0
    for char in range(len(string)):
       new_string.append(string[char])
       if cont <= 8:
        new_string == ""
       cont = cont + 1
    return ''.join(new_string)

def RetCam(string): #Retorna o Caminho Baseado No Codigo
    Cod = string
    Cod = int(Cod)
    arquivo = open('DATA.txt', 'r')
    Cod = (Cod * 5) - 2
    cont = 1
    while cont <= Cod:
        linha = arquivo.readline()  
        cont = cont + 1
    arquivo.close()
    linha = linha.replace("Caminho: ","")
    return linha
    
def RetCod(): #Retorna o ultimo codigo do programa
    CONT = open('CONT.txt', 'r')
    conta = CONT.readline()
    conta = int(conta) + 1
 
    arquivo = open('CONT.txt', 'r')
    arquivo.close()    

    arquivo = open('CONT.txt', 'w')
    conta = str(conta)
    arquivo.write(conta)
    arquivo.close()

    return conta

#==============================================MAIN==============================================
Menu()



