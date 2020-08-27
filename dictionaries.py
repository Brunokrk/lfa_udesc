import inputs as infnc
import transition as transfnc
import minimizer as minfnc

def add_list(dictionary, pu, pv, qu, qv):
    """Função que cria ou adiciona listas para posterior verificação"""
    lista = [qu, qv]
    if (pu+pv) not in dictionary.keys():
        # lista ainda não existe
        dictionary[pu+pv] = []
        dictionary[pu+pv].append(lista)
        print("Lista encabeçada por("+str(pu)+","+str(pv)+") criada")
    else:
        # lista ja existe
        dictionary[pu+pv].append(lista)
        print("Lista encabeçada por("+str(pu)+","+str(pv) +
              ") atualizada com ("+str(lista[0])+","+str(lista[1])+")")

def tops_a_list (dictionary, table, qu, qv):
    """Função que marca as posições da lista""" 
    for value in dictionary[qu+qv]:
        #primeiro, marcar toda a lista
        coord_i_a = get_coord_i_column(table, value[0])
        coord_j_a = 0
        coord_i_b = (len(table)-1)
        coord_j_b = get_coord_j_line(table, value[1])
        minfnc.mark_table(table, coord_i_a, coord_j_b)
    for item in dictionary[qu+qv]:
        if check(dictionary, table, value[0], value[1]):
            tops_a_list(dictionary, table,value[0], value[1])

def check (dictionary,table, qu, qv):
    """Verifica se o elemento que entrou encabeça ou não uma lista"""
    if (qu+qv) in dictionary.keys():
        return True
    else:
        return False

def get_coord_i_column(table, a):
    """Retorna endereço i na tabela"""
    for i in table:
        if table[i][0] == a:
            return i
        
def get_coord_j_line(table, a):
    """Retorna endereço j na tabela"""
    for j in table[-1]:
        if table[-1][j] == a:
            return j
    