class Common_State():
    """Modelagem dos estados que não são finais nem iniciais"""

    def __init__(self, goes_to, n_gt):
        """Construtor"""
        self.goes_to = goes_to #dictionaty with all transitions of this node
        self.n_gt = n_gt    #numero de transições para outros estados
    

