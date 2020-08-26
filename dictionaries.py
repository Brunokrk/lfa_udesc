import inputs as infnc
import transition as transfnc
# Rules:
# Função que verifica se um par (Qu, Qv) encabeçam uma lista


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
