# variavel com a palavra secreta
palavra_secreta = input("Digite a palavra secreta: ")

# cria uma variavel de texto chamada resultado com "_" correspondentes a
# quantidade de letras da palavra secreta
resultado = []
for posicao in range(1, len(palavra_secreta) + 1):
    resultado.append("_")

# mostra os "_" correspondentes a quantidade de letras da palavra secreta
print("Palavra secreta:", " ".join(resultado))

jogo_acabou = False
chutes_certos = ""
erros = 0

# impede o programa de acabar
while jogo_acabou == False:
    # cria uma variavel pra guardar a letra que a pessoa digitar
    letra_chute = input("Dá seu chute ai: ")

    # verifica se a letra digitada pelo usuario está dentro da palavra secreta
    if letra_chute in palavra_secreta:

        for posicao_da_letra in range(0, len(palavra_secreta)):

            if palavra_secreta[posicao_da_letra] == letra_chute:
                resultado[posicao_da_letra] = letra_chute

        print(" ".join(resultado).upper())
    else:
        print("Tente novamente! =(")
        erros += 1

    if "_" not in resultado:
        print("Você ganhou!")
        jogo_acabou = True

    if erros == 3:
        print("Cê si fudeu!")
        jogo_acabou = True
