import automaton as atm
import functions as fnc
from stack import Stack

epsilon = "&"
verifi = "?"

data = fnc.open_json() #abre arquivo
pilha = Stack() #criando pilha do automato
words_to_aprove = data.get("aprovar") #lote de palavras para aprovar
words_to_reject = data.get("rejeitar")#lote de palavras para rejeitar
init_state = data.get("init_state")#estado inicial
final_states = data.get("final_states")#estados finais
actual_state = init_state

#Coletando todos os estados e suas transições
all_states = []
for state_item in data["all_states"]:
    transitions = []
    for transition_item in state_item.get("transitions"):
        transition = atm.Transition(transition_item.get("letter"), transition_item.get("unstack"), transition_item.get("stack_up"), transition_item.get("goes_to"))
        transitions.append(transition)
    state = atm.State(state_item.get("state"), transitions)
    all_states.append(state)


print(words_to_aprove)
print(words_to_reject)
print(init_state)
print(final_states)
print(actual_state)
print(all_states[0].transitions)