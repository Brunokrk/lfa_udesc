import sys
def alfabeto():
    """Coleta o alfabeto"""
    alfabeto = input("Informe o alfabeto na forma abcd: ")
    if alfabeto == '':
        print("ERRO :: NENHUM ALFABETO INSERIDO")
        sys.exit()
    return alfabeto.lower()

def estados():
    """Coleta os estados do automato"""
    all_states = input("Informe os estados possíveis na forma ABCDEF: ")
    if all_states == '':
        print("ERRO :: NENHUM ESTADO INSERIDO")
        sys.exit()
    return all_states.upper()

def estados_finais():
    """Coleta os estados finais do automato"""
    final_states = input("Informe os estados finais do AFD na forma ABCD: ")
    if final_states == '':
        print("ERRO :: NENHUM ESTADO INSERIDO")
        sys.exit()
    return final_states.upper()

def estados_iniciais():
    """Coleta os estados iniciais do automato"""
    init_state = input("Informe o estado inicial do AFD: ")
    if init_state== '':
        print("ERRO :: NENHUM ESTADO INSERIDO")
        sys.exit()
    return init_state.upper()

def estados_equivalentes(a, b):
    """Define as letras que representarão os estados equivalentes"""
    msg = "Informe a Letra que substituirá os estados equivalentes " + a +" e "+ b +":"
    new_state = input(msg)
    if new_state == '':
        print("ERRO :: NENHUM ESTADO INSERIDO")
        sys.exit()
    return new_state.upper()
    
def print_quint(all_states, alfabeto, final_states, init_state):
    """Mostra a quintupla do automato """
    print("----5-TUPLA do AFD----")
    print("M = ({"+str(alfabeto)+"},{"+str(all_states)+"}, P,"+str(init_state)+",{"+ str(final_states)+"})")