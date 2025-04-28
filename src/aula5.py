import random

def gerar_numero_secreto():
    return random.randint(1, 10)

def verificar_palpite(numero_secreto, palpite):
    return palpite == numero_secreto

def incrementando(numero):
    return numero + 1

def duplicando(numero):
    return numero * 2

def main():
    numero_secreto = gerar_numero_secreto()
    palpite = int(input("Tente adivinhar o número de 1 a 10: "))
    
    if verificar_palpite(numero_secreto, palpite):
        print("Parabéns! Você acertou!")
    else:
        print(f"Errou! O número era {numero_secreto}.")
    
    print(f"Seu número incrementado é", incrementando(palpite))
    print(f"Seu número duplicado é", duplicando(palpite))



if __name__ == "__main__":
    main()