import inputs as infnc
import minimizer as minfnc
import sys


def init_matriz(all_states, alfabeto):
    """ (str,str) -> matriz onde a primeira linha é o alfabeto
    e a primeira coluna são os estados finais """
    it = 0
    jt = 0
    matriz = []
    for i in range(0, (len(all_states)+1)):
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
    for i in range(0, (len(all_states) + 1)):
        for j in range((len(alfabeto) + 1)):
            print("["+str(matriz[i][j])+"]", end='')
        print()
    print("---------------------------------")


def program_function(matriz, all_states, alfabeto):
    """Completa a matriz de transição do automato"""
    flag = True
    for i in range(1, (len(all_states) + 1)):
        for j in range(1, (len(alfabeto) + 1)):
            transition = "Informe a transição P(" + \
                matriz[i][0]+","+matriz[0][j]+"): "
            matriz[i][j] = str(input(transition)).upper()
            if(matriz[i][j] == ''):
                # nenhuma transição para entrada
                print("\nERRO ::: A FUNÇÃO PROGRAMA DEVE SER TOTAL")
                sys.exit()
            if(len(matriz[i][j]) >= 2):
                print("\n ERRO ::: O AUTÔMATO DEVE SER DETERMINÍSTICO, UM ESTADO NÃO PODE ATINGIR MAIS DE 1 ESTADO APENAS COM UMA ENTRADA")
                print("Erro detectado, programa finalizado")
                sys.exit()


def construct_new_program_function(matriz, table, all_states, alfabeto, final_states):
    """Função dedicada á construção da tabela de transições do autômato minimizado"""
    dict_eqst = minfnc.identifies_equivalent_states(
        table, all_states, alfabeto)

    for i in range(1, (len(all_states) + 1)):
        for j in range((len(alfabeto) + 1)):
            for k in dict_eqst:
                if matriz[i][j] in dict_eqst[k]:
                    matriz[i][j] = k

    return dict_eqst


def otimizate_new_program_function(matriz):
    """Exclusão dos estados inúteis"""
    new_matriz = []
    for i in matriz:
        if i not in new_matriz:
            new_matriz.append(i)

    for i in range(0, len(new_matriz)):
        for j in range(0, len(new_matriz[1])):
            print("["+str(new_matriz[i][j])+"]", end='')
        print()
    print("---------------------------------")
    return new_matriz


def new_states(new_matriz):
    """Função que retorna os novos estados"""
    new_all_states = []
    for i in range(1, len(new_matriz)):
        new_all_states.append(new_matriz[i][0])
    return new_all_states


def new_f_states(new_all_states, final_states, dicio):
    """Função que retorna os novos estados finais"""
    aux = []
    new_final_states = []
    for j in range(0, len(final_states)):
        aux.append(str(final_states[j]))

    for i in range(0, len(aux)):
        for k in dicio:
            if aux[i] in dicio[k]:
                aux[i] = k

    for i in aux:
        if i not in new_final_states:
            new_final_states.append(i)

    return new_final_states


def new_i_state(init_state, dicio):
    """Função que retorna novo estado final"""
    for k in dicio:
        if init_state in dicio[k]:
            init_state = k
    return init_state
