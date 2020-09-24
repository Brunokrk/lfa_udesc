from json import load

def open_json():
    with open('./interpretador_ap/entrada.json','r') as json_file:
        data = load(json_file)
    return data




def calculate(all_states, init_state, final_states, actual_state,word, pilha):
    """Calcula as devidas transições"""
    epsilon = "&"
    verifi = "?"

    if len(word) >= 1:
        #atualiza palavra de entrada e letra a ser processada
        actual_letter = word[0]
        word = word[1:]
    else:
        #palavra vazia
        actual_letter = None
    
    estado_atual = [state for state in all_states if state.state == actual_state][0]

    if actual_letter == None:
        for transition in estado_atual.transitions:
            if transition.letter == verifi:
                if transition.unstack == verifi:
                    if len(pilha) == 0:
                        if transition.goes_to in final_states:
                            actual_state = transition.goes_to
                            return True
                elif pilha.peek() == transition.unstack:
                    pilha.pop()
                    if transition.stack_up != epsilon:
                        pilha.push([str(item) for item in transition.stack_up])
                    actual_state = transition.goes_to
                    return True
        return False

    for transition in estado_atual.transitions:
        if transition.letter == actual_letter:
            if epsilon == transition.unstack:
                if transition.stack_up != epsilon:
                    pilha.push([str(item) for item in transition.stack_up])
                actual_state = transition.goes_to
                return True
            elif len(pilha) > 0 and pilha.peek()==transition.unstack:
                pilha.pop()
                if transition.stack_up != epsilon:
                    pilha.push([str(item) for item in transition.stack_up])
                actual_state = transition.goes_to
                return True
            elif transition.unstack == verifi and len(pilha)==0:
                if transition.stack_up != epsilon:
                    pilha.push([str(item) for item in transition.stack_up])
                    actual_state = transition.goes_to
                    return True
    return False

