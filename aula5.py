import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Tente adivinhar o número de 1 a 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print(f"Errou! O número era {numero_secreto}.")
    print("Tente novamente")