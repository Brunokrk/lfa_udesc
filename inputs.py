def alfabeto():
    alfabeto = input("Informe o alfabeto na forma abcd: ")
    return alfabeto

def estados():
    all_states = input("Informe os estados possíveis na forma ABCDEF: ")
    return all_states

def estados_finais():
    final_states = input("Informe os estados finais do AFD na forma ABCD: ")
    return final_states

def estados_iniciais():
     init_state = input("Informe o estado inicial do AFD: ")
     return init_state

def estados_equivalentes(a, b):
    msg = "Informe a Letra que substituirá os estados equivalentes " + a +" e "+ b +":"
    new_state = input(msg)
    return new_state