def start(fita, size, pilha):
    cont = 0
    initial_state(cont, fita, size, pilha)

def initial_state(cont, fita, size, pilha):
    """Estado in inicial"""
    if (fita[cont] == '1'):
        cont = cont + 1
        pilha.push("0")
        state_d(cont, fita, size, pilha)
    elif(fita[cont] == '0'):
        cont = cont +1
        pilha.push("1")
        state_b(cont, fita, size, pilha)


def state_d(cont, fita, size, pilha):
    """Estado D"""
    if (fita[cont] == "1"):
        cont = cont +1
        pilha.push("0")
        state_d(cont, fita, size, pilha)
    elif(fita[cont] == "0"):
        cont = cont + 1
        pilha.pop()
        state_e(cont, fita, size, pilha)

def state_e (cont, fita, size, pilha):
    """Estado E"""
    if(cont > len(fita)-1 and len(pilha)==0):
        final_state()
        return
    if(cont > len(fita)-1 and len(pilha)!=0):
        print("FITA:::INVÁLIDA")
        return
    if(fita[cont] == "0" and pilha.peek()=="0"):
        #(0,0,e)

        cont = cont+1
        pilha.pop()
        state_e(cont, fita, size, pilha)
    elif(fita[cont] == "0" and len(pilha) == 0):
        #(0,?,1)
        cont = cont +1
        pilha.push("1")
        state_e(cont, fita, size, pilha)
    elif(fita[cont] == "0" and pilha.peek()=="1"):
        #(0, 1,11)
        cont = cont+1
        pilha.push("1")
        state_e(cont, fita, size, pilha)
    elif(fita[cont] == "1" and pilha.peek()=="1"):
        #(1, 1,e)
        cont = cont+1
        pilha.pop()
        state_e(cont, fita, size, pilha)
    elif(fita[cont] == "1" and len(pilha)==0):
        #(1, ?,0)
        cont = cont+1
        pilha.push("0")
        state_e(cont, fita, size, pilha)
    elif(fita[cont] == "1" and pilha.peek()=="0"):
        #(0, 1,11)
        cont = cont+1
        pilha.push("0")
        state_e(cont, fita, size, pilha)
def state_b(cont, fita, size, pilha):
    if (fita[cont] == "0"):
        cont = cont +1
        pilha.push("1")
        state_b(cont, fita, size, pilha)
    elif(fita[cont] == "1"):
        cont = cont + 1
        pilha.pop()
        state_c(cont, fita, size, pilha)

def state_c (cont, fita, size, pilha):
    """Estado E"""
    if(cont > len(fita)-1 and len(pilha)==0):
        final_state()
        return
    if(cont > len(fita)-1 and len(pilha)!=0):
        print("FITA:::INVÁLIDA")
        return
    if(fita[cont] == "1" and pilha.peek()=="1"):
        #(1,1,e)
        cont = cont+1
        pilha.pop()
        state_c(cont, fita, size, pilha)
    elif(fita[cont] == "1" and len(pilha) == 0):
        #(1,?,0)
        cont = cont +1
        pilha.push("0")
        state_c(cont, fita, size, pilha)
    elif(fita[cont] == "1" and pilha.peek()=="0"):
        #(1, 0,00)
        cont = cont+1
        pilha.push("0")
        state_c(cont, fita, size, pilha)
    elif(fita[cont] == "0" and pilha.peek()=="0"):
        #(0, 0,e)
        cont = cont+1
        pilha.pop()
        state_c(cont, fita, size, pilha)
    elif(fita[cont] == "0" and len(pilha)==0):
        #(0, ?,1)
        cont = cont+1
        pilha.push("1")
        state_c(cont, fita, size, pilha)
    elif(fita[cont] == "0" and pilha.peek()=="1"):
        #(0, 1,11)
        cont = cont+1
        pilha.push("1")
        state_c(cont, fita, size, pilha)

def final_state():
    print("FITA:::VÁLIDA")