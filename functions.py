import inputs as infnc


def init_matriz(all_states, alfabeto):
    ''' (str,str) -> matriz onde a primeira linha é o alfabeto
    e a primeira coluna são os estados finais '''
    it = 0
    jt = 0
    matriz = []
    for i in range(0,(len(all_states)+1)):
        linha = []
        for j in range(0, (len(alfabeto)+1)):
            if (j == 0 and i != 0):
                linha.append(all_states[it])
                it = it+1
            elif(i == 0 and j != 0):
                linha.append(alfabeto[jt])
                jt = jt+1
            else:
                linha.append('*')
        matriz.append(linha)

    return matriz


def print_actual_prfn(matriz, all_states, alfabeto):
    print("---FUNÇÃO PROGRAMA ATUAL---")
    for i in range((len(all_states) +1)):
        for j in range((len(alfabeto) +1)):
            print(matriz[i][j], end='')
        print()
    print("---------------------------")

def program_function(matriz, all_states, alfabeto):
    flag = True
    for i  in range(1, (len(all_states) +1)):
        for j in range(1, (len(alfabeto) +1)):
            transition = "Informe a transição P("+matriz[i][0]+","+matriz[0][j]+"): " 
            matriz[i][j] = str(input(transition))

    #tentar juntar esta função com a init_matriz
    





# def update_prfn(alfabeto, all_states):


alfabeto = infnc.alfabeto()
all_states = infnc.estados()
init_state = infnc.estados_iniciais()
final_states = infnc.estados_finais()

matriz = init_matriz(all_states, alfabeto)
print_actual_prfn(matriz, all_states, alfabeto)
program_function(matriz, all_states, alfabeto)
print_actual_prfn(matriz, all_states, alfabeto)