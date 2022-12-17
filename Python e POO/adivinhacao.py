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

num = int(input("Digite um numero: "))

acertou = (num == num_secreto)
menor   = (num < num_secreto)
maior   = (num > num_secreto)

if(acertou):
    print("Você acertou :)")
elif(menor):
    print("Você chutou um numero menor")
elif(maior):
    print("Você chutou um numero maior")

print("------------FIM DE JOGO------------")