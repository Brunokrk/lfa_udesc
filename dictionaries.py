import inputs as infnc
import transition as transfnc
#Rules:
#Função que verifica se um par (Qu, Qv) encabeçam uma lista
#Função que adicione uma lista encabeçada por 
# (pu,pv) = ['QuQv']


def unmarked (dict, pu, pv, qu, qv):
    
    dict[pu+pv] = [qu+qv] 
    return dict