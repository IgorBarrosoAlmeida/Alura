'''
 * @File adivinhacao.py
 * @Author Igor Barroso Almeida
 * @Brief Jogo de adivinhação criado
 * no curso de introdução ao python da Alura
 * @Date 14/12/2022 
'''

print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!!")
print("-----------------------------------")

num_secreto = 42
max_tentativas = 3
rodada = 1

while (rodada <= max_tentativas):
    print(f"Tentativa {rodada} de {max_tentativas}")
    num = int(input("Digite um numero: "))

    acertou = (num == num_secreto)
    menor   = (num < num_secreto)
    maior   = (num > num_secreto)

    if(acertou):
        print("Você acertou :)")
        break
    elif(menor):
        print("Você chutou um numero menor")
    elif(maior):
        print("Você chutou um numero maior")
    rodada += 1

print("------------FIM DE JOGO------------")