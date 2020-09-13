from pilha import Pilha
import automato as atm

flag = "exit"
k = 0
while(1):
    fita = input("Informe a fita:   ")
    if (fita == flag):
        print("Finalizando...")
        break
    else:
        size = len(fita) - 1  # começando em 0
        pilha = Pilha()
        atm.start(fita, size, pilha)
