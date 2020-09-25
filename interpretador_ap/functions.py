from json import load
from fita import Word

def open_json():
    with open('./interpretador_ap/entrada.json', 'r') as json_file:
        data = load(json_file)
    return data


def calculate(all_states, final_states, actual_state, obj_word, pilha):
    """Calcula as devidas transições"""
    epsilon = "&"
    verifi = "?"

    actual_letter = None
    if len(obj_word.word)> 1:
        actual_letter = obj_word.word[0]
        obj_word.word = obj_word.word[1:]
    elif len(obj_word) == 1:
        actual_letter = obj_word.word[0]
        obj_word.word = ""

    estado_atual = [
        state for state in all_states if state.state == actual_state.state][0]
    
    #print(str(estado_atual.state))

    if actual_letter == None:
        for transition in estado_atual.transitions:
            if transition.letter == verifi:
                if transition.unstack == verifi:
                    if len(pilha.stack) == 0:
                        if transition.goes_to in final_states:
                            actual_state.state = transition.goes_to
                            return True
                elif pilha.stack[-1] == transition.unstack:
                    pilha.stack.pop()
                    if transition.stack_up != epsilon:
                        pilha.stack.extend([item for item in transition.stack_up])
                    actual_state.state = transition.goes_to
                    return True
        return False

    for transition in estado_atual.transitions:
        print("teste")
        if transition.letter == actual_letter:
            if epsilon == transition.unstack:
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                actual_state.state = transition.goes_to
                return True
            elif (len(pilha.stack) > 0) and (pilha.stack[-1] == transition.unstack):
                print("FOI AGORA ESSA PORRA?")
                pilha.stack.pop()
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                actual_state.state = transition.goes_to
                return True
            elif transition.unstack == verifi and len(pilha.stack) == 0:
                if transition.stack_up != epsilon:
                    pilha.stack.extend([item for item in transition.stack_up])
                    actual_state.state = transition.goes_to
                    print("retorno 1")
                    print("Empilhou "+str(pilha.stack[-1]))
                    return True
    return False


def confirmating(all_states, init_state, final_states, actual_state):
    """Confirmando autômato inserido"""
    print("Estados e suas transições")
    print("--------------------------------------")
    for state in all_states:
        if(len(state.transitions) == 0):
            print("Estado("+str(state.state).upper()+")")
            print("Este estado não possui nenhuma transição")
            print("--------------------------------------")
        else:
            print("Estado("+str(state.state).upper()+")")
            print("Transições:"+str(state.transitions) + ".")
            print("--------------------------------------")

def approving_words(all_states, final_states, actual_state, words_to_aprove, pilha):
    """Função dedicada á aprovação das palavras"""
    for word in words_to_aprove:
        obj_word = Word(word)
        flag = True
        while flag:
            print(obj_word.word)
            flag = calculate(all_states, final_states, actual_state, obj_word, pilha)
            print(actual_state.state)
            #print(actual_state.state)
            #print(pilha)
            
        if len(obj_word.word)==0 and len(pilha) == 0 and actual_state.state in final_states:
            print("! APROVADA !")
        else:
            print("ERROR::FITA INVÁLIDA")
