import inputs as infnc
import minimizer as minfnc

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
                linha.append('-')
        matriz.append(linha)

    return matriz

def print_actual_prfn(matriz, all_states, alfabeto):
    """Printa a matriz de transição do automato"""
    print("------FUNÇÃO PROGRAMA ATUAL------")
    for i in range(0,(len(all_states) +1)):
        for j in range((len(alfabeto) +1)):
            print("["+str(matriz[i][j])+"]", end='')
        print()
    print("---------------------------------")

def program_function(matriz, all_states, alfabeto):
    """Completa a matriz de transição do automato"""
    flag = True
    for i  in range(1, (len(all_states) +1)):
        for j in range(1, (len(alfabeto) +1)):
            transition = "Informe a transição P("+matriz[i][0]+","+matriz[0][j]+"): " 
            matriz[i][j] = str(input(transition))

def construct_new_program_function(matriz, table, all_states, alfabeto):
    """Função dedicada á construção da tabela de transições do autômato minimizado"""
    dict_eqst = minfnc.identifies_equivalent_states(table, all_states, alfabeto) 

    for i in range(1, (len(all_states) +1)):
        for j in range((len(alfabeto) +1)):
            for k in dict_eqst:
                if matriz[i][j] in dict_eqst[k]:
                    matriz[i][j] = k
    

