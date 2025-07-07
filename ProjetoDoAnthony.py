''''
Lets Go Gambling!
2025.07.1
Anthony Pagani
'''

# OBJETIVO: Criar um Slot Machine que funciona quando eu clico play no programa

# Slot Machine

# Biblioteca
from random import choice

# Função do Slot Machine
def StartGambling():
    Fruit = ["cherry", "lemon", "orange", "apple"]  # Roletador dos simbolos 
    spin = [choice(Fruit) for _ in range(3)]  # Vai gerar 3 simbolos aleatorios
    print(f"spin: {spin}")  # resultado da saida do giro
    if spin[0] == spin[1] == spin[2]:  # Vai ver se os simbolos estão iguais
        print("I can't stop winning!")  # mensagem de que Vençeu
    else:
        print("AW, dang it...")  # mensagem de que perdeu

StartGambling()
