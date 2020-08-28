import inputs as infnc
import transition as transfnc
import minimizer as minfnc

# inputs do usuário
alfabeto = infnc.alfabeto()
all_states = infnc.estados()
init_state = infnc.estados_iniciais()
final_states = infnc.estados_finais()

# Gera matriz de transições
matriz = transfnc.init_matriz(all_states, alfabeto)
transfnc.program_function(matriz, all_states, alfabeto)
infnc.print_quint(all_states, alfabeto, final_states, init_state)
transfnc.print_actual_prfn(matriz, all_states, alfabeto)

# Gera tabela de minimização
table = minfnc.init_min_table(all_states)
minfnc.marcar_finais(table, all_states, final_states)
print("Após diferenciar os estados finais dos não finais:")
minfnc.print_actual_mintab(table, all_states)

# Executa a Minimização
minfnc.minimizer(matriz, table, all_states, alfabeto)
minfnc.print_actual_mintab(table, all_states)

# Nova tabela de transições
dictio = transfnc.construct_new_program_function(
    matriz, table, all_states, alfabeto, final_states)
print("Após todo cálculo, a Função programa do autômato resultante é a seguinte:")
transfnc.print_actual_prfn(matriz, all_states, alfabeto)
print("Excluindo-se os estados inúteis, ficamos com:")
new_matriz = transfnc.otimizate_new_program_function(matriz)

# Novas informações do automatô mínimo
new_all_states = transfnc.new_states(new_matriz)
new_final_states = transfnc.new_f_states(new_all_states, final_states, dictio)
new_init_state = transfnc.new_i_state(init_state, dictio)
infnc.print_quint(new_all_states, alfabeto, new_final_states, new_init_state)
input()
