import random

def jogar():
    boas_vindas()
    palavra_secreta, palavra_encontrada = escolhe_palavra() #vendo se funcionou o .gitignore
    erros = 0
    while(True):
        print(''.join(palavra_encontrada))
        chute = inputs()
        palavra_encontrada, erros = checagem(palavra_secreta, palavra_encontrada, chute, erros)
        if (fugas_do_loop(palavra_encontrada, palavra_secreta, erros)):
            break

def boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolhe_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta, ["_" for letra in palavra_secreta]

def inputs():
    while(True):
        chute = input("Qual letra? ")
        if len(chute) > 1:
            print("Escreva somente uma letra!")
            continue
        return chute


def checagem(palavra_secreta, palavra_encontrada, chute, erros):
    if (palavra_secreta.find(chute) == -1):
        erros += 1
        print(f"Não encontrei a letra {chute} na palavra! Erro {erros} de 10")
        return palavra_encontrada, erros
    else:
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                palavra_encontrada[index] = chute.lower()
            index += 1
    return palavra_encontrada, erros

def fugas_do_loop(palavra_encontrada, palavra_secreta, erros):
    if ("_" not in palavra_encontrada):
        print("Parabéns! Você acertou a palavra {}!".format(palavra_secreta))
        return True

    if (erros == 10):
        print("Que pena! Não encontrou a palavra {}! :(".format(palavra_secreta))
        return True

if(__name__ == "__main__"):
    jogar()