from pilha import Pilha
import automato as atm

alphabet = atm.get_alphabet()
atm.check_intention(alphabet)
all_states = atm.get_all_states()
atm.check_intention(all_states)
init_state = atm.get_init_state()
atm.check_intention(init_state)
final_state = atm.get_final_state()
atm.check_intention(final_state)
stack_alphabet = atm.get_stack_alphabet()
atm.check_intention(stack_alphabet)

vet = atm.get_transitions(all_states)
print(vet)