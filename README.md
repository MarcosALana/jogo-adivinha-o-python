# Jogo de Adivinhação em Python

Programa em Python onde o computador escolhe um número **aleatório entre 1 e 100** e o usuário tenta adivinhar.  
A cada palpite, o programa informa se o número secreto é **maior** ou **menor**.  
Ao acertar, mostra a quantidade de **tentativas** usadas.

## 🚀 Código principal
```python
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

📌 O que foi aprendido
Uso da biblioteca random para gerar números aleatórios (randint).
Laço while para repetir até uma condição ser atendida.
Condicionais if/elif/else para dar dicas ao usuário.
Validação de entrada com try/except para evitar erros ao converter texto em número.
Regras simples de UX no console (mensagens claras, limites de 1 a 100).

💭 Comentário pessoal

Foi divertido criar um jogo de adivinhação!
Gostei de trabalhar com número aleatório e validação de entrada, deixando o programa robusto e mais “inteligente”.
Senti a lógica ficando mais natural, e já consigo imaginar variações (limitar tentativas, ranking, níveis de dificuldade).
