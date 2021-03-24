######################################################################################
# NODES
######################################################################################



class NumberNode:
    def __init__(self,tok,identifier=False):
        self.tok=tok
        self.isident = identifier
    def __repr__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self,leftnode, optok, rightnode):
        self.left_node=leftnode
        self.right_node=rightnode
        self.op_tok=optok
    def __repr__(self):
        return f'({self.left_node},{self.op_tok},{self.right_node})'

class UnaryOpNode:
    def __init__(self,op_tok,node):
        self.op_tok=op_tok
        self.node=node
    def __repr__(self):
        return f'({self.op_tok},{self.node})'