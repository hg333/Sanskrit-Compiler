from nodes import NumberNode, BinOpNode, UnaryOpNode

DIG ='1234567890'


TT_INT ='INT'
TTMUL = 'MUL'
TTPLUS = 'PLUS'
TTDIV = 'DIV'
TTMINUS = 'MINUS'
TTLPAREN = 'LPAREN'
TTRPAREN = 'RPAREN'
TTNDEF = 'NDEF'

TTIDENTIFIER = 'IDENTIFIER'
TTKEYWORD = 'KEYWORD'
TTEQ = 'EQ'

TTEE='EE'
TTNE='NE'
TTLT='LT'
TTGT='GT'
TTLTE='LTE'
TTGTE='GTE'

TTAND ='AND'
TTOR = 'OR'
TTVAR = 'VAR'
TTNOT = 'NOT'
TTIF = 'IF'
TTWHILE = 'WHILE'
TTFOR = 'FOR'
TTTHEN = 'THEN'
TTELSE = 'ELSE'
TTELIF = 'ELIF'

TTNEWLINE = 'NEWLINE'
TTEOF= 'EOF'

TTINPUT = 'IN'
TTOUTPUT = 'OUT'

TTLBRACE = 'LBRACE'
TTRBRACE = 'RBRACE'
KEYWORDS=[
    TTVAR,
    TTAND,
    TTOR,
    TTNOT,
    TTFOR,
    TTWHILE,
    TTIF,
    TTTHEN,
    TTELIF,
    TTELSE,
    TTINPUT,
    TTOUTPUT
]
def operation(v1,v2,type,symbol_table,id):
    #print(v1,v2,type)
    if type==TTMUL:
        return v1*v2
    elif type==TTPLUS:
        return v1+v2
    elif type==TTMINUS:
        return v1-v2
    elif type==TTDIV:
        try: return v1//v2
        except: return "Divison by zero"
    elif type == TTEQ:
        symbol_table.set(id,v2)
        return v2
    elif type ==TTEE:
        return v1==v2
    elif type ==TTGTE:
        return v1>=v2
    elif type == TTLTE: return v1<=v2
    elif type == TTLT: return v1<v2
    elif type == TTGT: return v1>v2
    elif type == TTNE: return v1 !=v2
    elif type == TTAND: return v1 and v2
    elif type == TTOR: return v1 or v2
    else:
        pass


def interpretter(tree, symbol_table):
    #print(tree)
    if isinstance(tree, NumberNode):
        return tree.tok.value
    elif isinstance(tree, UnaryOpNode):
        #print(tree,tree.op_tok,tree.node)
        if str(tree.op_tok) == TTIF:
            for i in tree.node:
                if(interpretter(i[0],symbol_table)): return interpretter(i[1],symbol_table)
            return 0
        elif str(tree.op_tok) ==TTWHILE:
            ret = 0
            while(interpretter(tree.node[0],symbol_table)):
                #print(tree.node[1])
                ret = interpretter(tree.node[1],symbol_table)
            return ret
        elif str(tree.op_tok) == TTINPUT:
            #print("COOL")
            inp = int(input())
            symbol_table.set(tree.node.value,inp)
            return inp
        elif str(tree.op_tok) == TTOUTPUT:
            print(symbol_table.get(tree.node.value))
            return symbol_table.get(tree.node.value)
        val = interpretter(tree.node,symbol_table)
        if str(tree.op_tok)==TTMINUS:
            val=-val
        elif str(tree.op_tok) ==TTNOT:
            val = not val
        
        return val
    elif isinstance(tree, list):
        val =0
        for i in tree:
            val = interpretter(i,symbol_table)
        return val
    else:
        v1=interpretter(tree.left_node,symbol_table)
        v2=interpretter(tree.right_node,symbol_table)
        return operation(symbol_table.get(v1),symbol_table.get(v2),str(tree.op_tok),symbol_table,v1)