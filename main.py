# Dia 5 - Jogo de Adivinhação

import random

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Seu palpite: "))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro (ex.: 42).")
        continue

    if palpite < 1 or palpite > 100:
        print("Por favor, digite um número entre 1 e 100.")
        continue

    tentativas += 1

    if palpite < numero_secreto:
        print("Quase! O número secreto é MAIOR.")
    elif palpite > numero_secreto:
        print("Passou! O número secreto é MENOR.")
    else:
        print(f"🎉 Acertou! O número era {numero_secreto}. Você usou {tentativas} tentativa(s).")
        break
