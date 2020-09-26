import automaton as atm
import functions as fnc

epsilon = "&"
verifi = "?"

arq = fnc.open_json()  # abre arquivo
pilha = atm.Pilha()  # criando pilha do automato
words_to_aprove = arq.get("aprovar")  # lote de palavras para aprovar
words_to_reject = arq.get("rejeitar")  # lote de palavras para rejeitar
init_state = arq.get("init_state")  # estado inicial
final_states = arq.get("final_states")  # estados finais
actual_state = atm.CurrentState(init_state)
user_option = arq.get("mostrar_pilha")
# Coletando todos os estados e suas transições
all_states = []
for state_item in arq["all_states"]:
    transitions = []
    for transition_item in state_item.get("transitions"):
        transition = atm.Transition(transition_item.get("letter"), transition_item.get(
            "unstack"), transition_item.get("stack_up"), transition_item.get("goes_to"))
        transitions.append(transition)
    state = atm.State(state_item.get("state"), transitions)
    all_states.append(state)

fnc.approving_words(all_states, final_states, actual_state,
                    words_to_aprove, pilha, user_option)

#fnc.rejecting_words(all_states, final_states, actual_state,
#                    words_to_reject, pilha, user_option)
