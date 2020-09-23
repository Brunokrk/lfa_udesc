from pilha import Pilha
import automato as atm

flag = "exit"

while(1):
    word = input("palavra: ")
    if word == flag:
        break
    else:
        pilha = Pilha()
        atm.start(word, len(word), pilha)

