import inputs as infnc
import transition as transfnc

def init_min_table(all_states):
    """Cria a tabela de minimização onde serão marcados os estados distinguíveis"""
    table = []
    a = 0
    b = 1
    # inicio dos indices das posições desconsideradas da tabela at = linhas bt = colunas
    at = 0
    bt = 2
    n_states = len(all_states)
    for i in range(0, n_states):
        line = []
        for j in range(0, n_states):
            if(j == 0 and i != (n_states - 1)):
                line.append(all_states[b])
                b = b + 1
            elif(i == (n_states - 1) and j != 0):
                line.append(all_states[a])
                a = a + 1
            elif((j>=i+2) or (i==n_states - 1 and j ==0)):
                # posições que não serão utilizadas na matriz
                line.append('-')
                at = at + 1
                bt = bt + 1
            else:
                line.append('*')
        table.append(line)
    return table


def print_actual_mintab(table, all_states):
    '''Printa a tabela de minimização do automato'''
    print("---TABELA DE MINIMIZAÇÃO ATUAL---")
    for i in range((len(all_states))):
        for j in range((len(all_states))):
            print("["+str(table[i][j])+"]", end='')
        print()
    print("---------------------------------")


def marcar_finais (table, all_states, final_states):
    n_states = len(all_states)
    n=0
    m=0
    for i in range(0, n_states):
        if table[i][0] in final_states:
            #achou um elemento final na coluna de elementos
            #marcar todos os elementos da linha i
            for  n in range (1, i+2):
                table [i][n] = "#"

    for j in range(1, n_states - 1):
        if table[n_states -1][j] in final_states:
            #achou um elemento final na linha de elementos
            #marcar todos os elementos da coluna j
            for n in range (j-1, n_states - 1):
                if (table[n][j] == "#"):
                    table[n][j] = "*"
                else:
                    table [n][j] = "#"

def minimizer (matriz, table, all_states, alfabeto):
    """Função que faz a minimização do automato"""
    n_states = len(all_states)
    for i in range((len(all_states))):
        for j in range((len(all_states))):
            if table[i][j] == "*" :
                #achou uma posição não marcada
                state_A = table[i][0] #estado na coluna
                state_B = table[n_states - 1][j] #estado na linha
                #checar interações com cada entrada
                vet_state_A = get_vet_state_A ( matriz, all_states, alfabeto, state_A)
                vet_state_B = get_vet_state_B(matriz, all_states, alfabeto, state_B)
                check_rules(table, all_states, vet_state_A, vet_state_B, alfabeto)
               #...

def check_rules (table,all_states, vet_state_A, vet_state_B, alfabeto):
    cont = 0
    for k in range(1, len(alfabeto)+1):
        if vet_state_A[k] == vet_state_B [k]:
            #Não marcar, são equivalentes
            print("pu = pv, para entrada ("+str(alfabeto[cont])+"), portanto são equivalentes e não serão marcados")
            print("P("+str(vet_state_A[0])+","+str(alfabeto[cont])+")-> "+ str(vet_state_A[k]))
            print("P("+str(vet_state_B[0])+","+str(alfabeto[cont])+")-> "+ str(vet_state_B[k]))
            cont = cont + 1
        elif vet_state_A[k] != vet_state_B[k]:
            #verificar se {pu,pv} estão marcados
            state_A = vet_state_A[k]
            state_B = vet_state_B[k]
            flag = check_mark(table, all_states, state_A, state_B)
            #Flag = true, marcado;
            #Flag = False, não marcado

def check_mark(table, all_states, state_A, state_B):
    #state_A = pu, state_B = pv
    n_states = len(all_states)
    if((state_A == all_states[0] and state_B == all_states[n_states-1]) or (state_B == all_states[0] and state_A == all_states[n_states-1])):
        #se state_A for o primeiro estado inserido e
        #se state_B for o último estado inserido
        if(table[n_states-1][1] == "#"):
            #está marcado
            print("O par ("+str(state_A)+", "+str(state_B)+"), está marcado")
            return True
        else:
            #não está marcado
            print("O par ("+str(state_A)+", "+str(state_B)+"), não está marcado")
            return False
    elif((state_A == all_states[0]) or (state_B == all_states[0])):
        #se state_A ou state_B for o primeiro estado
        for l in  range(0, n_states-1):
            if(table[l][0] == (state_B or state_A)):
                if(table[l][1]=="#"):
                    print("O par ("+str(state_A)+", "+str(state_B)+"), está marcado")
                    return True
                else:
                    print("O par ("+str(state_A)+", "+str(state_B)+"), não está marcado")
                    return False
    elif((state_A == all_states[n_states-1]) or (state_B == all_states[n_states-1])):
        #se state_A ou state_B for o ultimo estado
        for l in range(1, n_states):
            if(table[n_states - 1][l] == (state_A or state_B)):
                if(table[n_states-2][l] == "#"):
                    print("O par ("+str(state_A)+", "+str(state_B)+"), está marcado")
                    return True
                else:
                    print("O par ("+str(state_A)+", "+str(state_B)+"), não está marcado")
                    return False
    else:
        #Não são nem o primeiro nem o último
        for l in range(0, n_states-1):
            if(table[l][0] == state_A):
                coord_i = l
        
        for k in range(1, n_states):
            if(table[n_states - 1][k] == state_B):
                coord_j = k
        
        if(table[coord_i][coord_j] == "#"):
            print("O par ("+str(state_A)+", "+str(state_B)+"), está marcado")
            return True
        else:
            print("O par ("+str(state_A)+", "+str(state_B)+"), não está marcado")
            return False


                                
#Rules:
#P(Qu, a) = pu e P(Qv,a) = pv
#pu == pv (Qu equivalente a Qv, não marcar)

#pu != pv, e par {pu,pv} não está marcado (Qu, Qv) é incluído numa lista a partir de pu,pv

#pu != pv, e par {pu,pv} está marcado, (Qu, Qv) são não equivalentes, portanto marcar.
#se(Qu, Qv) encabeçam uma lista, marcar todos os pares da lista, e se algum par encabeça outra lista tbm
#

def get_vet_state_A (matriz, all_states, alfabeto, state_A):
    """Função que retorna o vetor de estados alcançados a partir do estado de entrada"""
    vet_state_A = []
    for k in range (1, len(all_states)+1):
        if matriz[k][0] == state_A:
            vet_state_A = matriz[k]
    return vet_state_A

def get_vet_state_B (matriz, all_states, alfabeto, state_B):
    """Função que retorna o vetor de estados alcançados a partir do estado de entrada"""
    vet_state_B = []
    for k in range (1, len(all_states)+1):
        if matriz[k][0] == state_B:
                vet_state_B = matriz [k]
    return vet_state_B