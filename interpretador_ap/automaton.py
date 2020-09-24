from typing import List
from collections import namedtuple
class State():
    """Modelagem de um único estado do automato"""
    def __init__(self, state, transitions: List[Transition]):
        self.state = state
        self.transitions = transitions

        
#Tupla com as informações de cada transição do Automato
Transition = namedtuple(
    'Transition', ["letter", "unstack", "stack_up", "goes_to"])
