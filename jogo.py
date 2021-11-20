# variavel com a palavra secreta
palavra_secreta = "caioba"

# cria uma variavel de texto chamada resultado com "_" correspondentes a
# quantidade de letras da palavra secreta
resultado = ""
for posicao in range(1, len(palavra_secreta) + 1):
    resultado += "_ "

# mostra os "_" correspondentes a quantidade de letras da palavra secreta
print("Palavra secreta:", resultado)

jogo_acabou = False
chutes_certos = ""

# impede o programa de acabar
while jogo_acabou == False:
    # cria uma variavel pra guardar a letra que a pessoa digitar
    letra_chute = input("Dá seu chute ai: ")

    resultado = ""

    # verifica se a letra digitada pelo usuario está dentro da palavra secreta
    if letra_chute in palavra_secreta:

        # armazena todos os chutes certos do usuário
        chutes_certos += letra_chute

        # para cada letra_da_palavra_secreta em/na palavra_secreta
        for letra_da_palavra_secreta in palavra_secreta:

            if letra_da_palavra_secreta == letra_chute:
                resultado += letra_chute + " "
            else:
                resultado += "_ "

        print(resultado)
    else:
        print("Tente novamente! =(")
