print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if chute> numero_secreto:
        print("Você errou!")

print("Fim do jogo")