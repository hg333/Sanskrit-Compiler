


import sys

original_stdout = sys.stdout # Save a reference to the original standard output
f= open('tac.txt', 'w')
sys.stdout = f




from nodes import NumberNode, BinOpNode, UnaryOpNode
DIG ='1234567890'
import basic

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
def operation(v1,v2,type,conditionals=False):
    global statement
    #print(v1,v2,type)
    cur = "v"+str(statement)
    statement+=1
    if type==TTMUL:
        print(cur,'=',v1,'*',v2,sep=' ')
    elif type==TTPLUS:
        print(cur,'=',v1,'+',v2,sep=' ')
    elif type==TTMINUS:
        print(cur,'=',v1,'-',v2,sep=' ')
    elif type==TTDIV:
        print(cur,'=',v1,'/',v2,sep=' ')
    elif type == TTEQ:
        print(v1,'=',v2,sep = ' ')
        return v1
    elif type ==TTEE:
        print(cur,'=',v1,'==',v2,sep=' ')
    elif type ==TTGTE:
        print(cur,'=',v1,'>=',v2,sep=' ')
    elif type == TTLTE: print(cur,'=',v1,'<=',v2,sep=' ')
    elif type == TTLT: print(cur,'=',v1,'<',v2,sep=' ')
    elif type == TTGT: print(cur,'=',v1,'>',v2,sep=' ')
    elif type == TTNE: print(cur,'=',v1,'!=',v2,sep=' ')
    elif type == TTAND: print(cur,'=',v1,'*',v2,sep=' ')
    elif type == TTOR: print(cur,'=',v1,'+',v2,sep=' ')
    else:
        pass
    return cur

statement = 1 

def code_generator(tree):
    global statement
    if isinstance(tree, NumberNode):
        return tree.tok.value
    elif isinstance(tree,UnaryOpNode):
        if(str(tree.op_tok) ==TTIF):
            li =[]
            for i in tree.node:
                k=code_generator(i[0])
                print("IF", k,"goto ifstatement"+str(statement))
                li.append(statement)
                statement+=1
            
            lst = statement
            print("goto ifstatement"+str(lst))
            statement+=1
            cur=0
            for i in tree.node:
                print("ifstatement"+str(li[cur]))
                k=code_generator(i[1])
                cur+=1
                print("goto ifstatement"+str(lst))
            print("ifstatement"+str(lst))
        
        elif str(tree.op_tok)==TTWHILE:
            cur = statement
            statement+=1
            print("whilestatement"+str(cur))
            cond = code_generator(tree.node[0])
            print("IFNOT",str(cond),"goto","endwhile"+str(cur),sep=' ')
            k=code_generator(tree.node[1])
            print("goto whilestatement"+str(cur))
            print("endwhile"+str(cur))
        elif str(tree.op_tok) ==TTMINUS:
            val= code_generator(tree.node)
            print(f'v{statement} = 0 - {val}')
            statement+=1
            return f'v{statement-1}'
        elif str(tree.op_tok) ==TTNOT:
            val= code_generator(tree.node)
            print(f'v{statement} = ! {val}')
            statement+=1
            return f'v{statement-1}'
        elif str(tree.op_tok) == TTINPUT:
            if(isinstance(tree.node,basic.Token)):
                print(f'input {tree.node.value}')
            else:
                print("SEMANTIC ERROR")
                return "SEMANTIC ERROR"
        
        elif str(tree.op_tok) == TTOUTPUT:
            if(isinstance(tree.node,basic.Token)):
                print(f'output {tree.node.value}')
            else:
                print("SEMANTIC ERROR")
                return "SEMANTIC ERROR"

    elif isinstance(tree,list):
        for i in tree:
            code_generator(i)
    else:
        v1 = code_generator(tree.left_node)
        v2 = code_generator(tree.right_node)
        return operation(v1,v2,str(tree.op_tok))
