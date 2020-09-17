from common_state import Common_State

def get_alphabet():
    """get alphabet"""
    alfabeto = input("Informe o alfabeto do Autômato: ")
    return alfabeto.lower()

def get_all_states():
    """get all states"""
    all_states = input("Informe todos os estados do Autômato: ")
    return all_states.upper()

def get_init_state():
    """gets init state"""
    init_state = input("Informe o estado inicial: ")
    return init_state.upper()

def get_final_state():
    """gets final state"""
    final_state = input("Informe o estado fnal: ")
    return final_state.upper()

def get_stack_alphabet():
    """gets alphabet"""
    stack_alphabet = input("Informe o alfabeto da pilha: ")
    return stack_alphabet.upper()

def check_intention(entrada):
    """Checa se usuário quer continuar"""
    if(entrada == "exit"):
        exit()
        
def get_transitions(all_states):
    """Pega as transições do autômato"""
    goes_to = {}
    flag = "/prox"

    for state in all_states:
        goes_to[state]= []
        while(1):
            value = input("(/prox para proximas transições) A transição vai de "+ str(state)+" para: ")
            
            if value == "/prox":
                break    
            valor = input("Transição: ")
            goes_to[state].append(value +  valor) 

    return goes_to

def deleting_dicio(dicio):
    """Deleta um dicionario"""
    dicio.clear()
    return dicio