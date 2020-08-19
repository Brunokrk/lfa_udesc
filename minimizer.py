import inputs as infnc


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
            elif(i >= at and j >= bt):
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
            print(table[i][j], end='')
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


