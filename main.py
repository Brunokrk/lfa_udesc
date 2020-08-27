import inputs as infnc
import transition as transfnc
import minimizer as minfnc

alfabeto = infnc.alfabeto()
all_states = infnc.estados()
init_state = infnc.estados_iniciais()
final_states = infnc.estados_finais()
matriz = transfnc.init_matriz(all_states, alfabeto)
transfnc.program_function(matriz, all_states, alfabeto)
infnc.print_quint(all_states, alfabeto, final_states, init_state)
transfnc.print_actual_prfn(matriz, all_states, alfabeto)
table = minfnc.init_min_table(all_states)
minfnc.marcar_finais(table, all_states, final_states)
print("Após diferenciar os estados finais dos não finais:")
minfnc.print_actual_mintab(table, all_states)
minfnc.minimizer(matriz, table, all_states, alfabeto)
minfnc.print_actual_mintab(table, all_states)
transfnc.construct_new_program_function(matriz, table, all_states, alfabeto)
print("Após todo cálculo, a Função programa do autômato resultante é a seguinte:")
transfnc.print_actual_prfn(matriz, all_states, alfabeto)
input()
