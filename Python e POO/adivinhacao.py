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

if(num == num_secreto):
    print("Você acertou :)")
else:
    print("Você errou ;-;")

print("------------FIM DE JOGO------------")