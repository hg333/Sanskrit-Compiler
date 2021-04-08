from nodes import NumberNode 
from nodes import BinOpNode 
from nodes import UnaryOpNode 
from interpretter import interpretter
from symboltable import SymbolTable
from intermediatecode import code_generator
import string
DIG ='1234567890०१२३४५६७८९'

LETTERS = string.ascii_letters+'अआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥'
LETTERS_DIGITS = LETTERS + DIG

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
TTVAR = '123 DELETED VAR'
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
class Token:
    def __init__(self,type_,value= None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos=-1
        self.current_char=None
        self.advance()
    def advance(self):
        self.pos+=1
        self.current_char = self.text[self.pos] if self.pos< len(self.text) else None
    def make_token(self):
        ret=[]
        #print("COOL",self.current_char)
        while self.current_char != None:
            if self.current_char in ' \t\n': self.advance()
            elif self.current_char =='+': ret.append(Token(TTPLUS)),self.advance()
            elif self.current_char =='-': ret.append(Token(TTMINUS)),self.advance()
            elif self.current_char =='*': ret.append(Token(TTMUL)),self.advance()
            elif self.current_char =='/': ret.append(Token(TTDIV)),self.advance()
            elif self.current_char ==')': ret.append(Token(TTRPAREN)),self.advance()
            elif self.current_char =='(': ret.append(Token(TTLPAREN)),self.advance()
            elif self.current_char in ';': ret.append(Token(TTNEWLINE)),self.advance()
            elif self.current_char =='{': ret.append(Token(TTLBRACE)),self.advance()
            elif self.current_char =='}': ret.append(Token(TTRBRACE)),self.advance()
            elif self.current_char =='!': 
                err,tok = self.make_not_equal()
                if not err: return err
                else: ret.append(tok)
            elif self.current_char =='=': 
                err,tok = self.make_equal()
                if not err: return err
                else: ret.append(tok)
            elif self.current_char =='>': 
                err,tok = self.make_gequal()
                if not err: return err
                else: ret.append(tok)
            elif self.current_char =='<': 
                err,tok = self.make_lequal()
                if not err: return err
                else: ret.append(tok)
            elif self.current_char in DIG:
                ret.append(self.make_number())
            elif self.current_char in LETTERS:
                ret.append(self.make_identifier())
            elif self.current_char.encode('utf-8') == b'\r':
                self.advance()
            else:

                print("YAKAMASHI!!!") 
                print(type(self.current_char),len(self.current_char))
                return 'Error in lexical analysis of '+  str(self.current_char.encode('utf-8'))
            #print(ret[-1])
        return ret

    def make_not_equal(self):
        self.advance()
        if(self.current_char == '='): 
            self.advance()
            return True,Token(TTNE)
        else: return False,Token(TTNDEF)
    def make_equal(self): 
        self.advance()
        if(self.current_char == '='): 
            self.advance()
            return True,Token(TTEE)
        else: return True,Token(TTEQ)
    def make_lequal(self): 
        self.advance()
        if(self.current_char == '='): 
            self.advance()
            return True,Token(TTLTE)
        else: return True,Token(TTLT)
    def make_gequal(self):
        self.advance()
        if(self.current_char == '='): 
            self.advance()
            return True,Token(TTGTE)
        else: return True,Token(TTGT)
    def make_identifier(self):
        ret=''
        ret+= self.current_char
        self.advance()

        while(self.current_char!=None and self.current_char in LETTERS_DIGITS + '_'):
            ret+=self.current_char 
            self.advance()

    
        if(str(ret) in KEYWORDS):
            return Token(ret)
        return Token(TTIDENTIFIER,ret)
    def make_number(self):
        ret=''
        while(self.current_char != None and self.current_char in DIG): 
            ret+=self.current_char
            self.advance()
        return Token(TT_INT,int(ret))


########################################### PARSER

##############################################
MAKEPERROR = 333
class Parser:
    def __init__(self,tokens):
        #print(tokens)
        self.tokens=tokens
        self.idx=-1
        self.cur_tok=None
        self.tot=0
        self.advance()
    def advance(self):
        self.idx+=1
        if self.idx< len(self.tokens): 
            self.cur_tok=self.tokens[self.idx]
        else: self.cur_tok =Token(TTNDEF)
        return self.cur_tok


    def pasrse(self):
        res=self.statements()
        return res

    def makeifcond(self):
        self.advance()
        ret=[]
        cond = self.cmp()
        if str(self.cur_tok) not in (TTTHEN): 
            self.tot+=MAKEPERROR
            return ret
        self.advance()
        self.tot+=1
        cons = self.cmp()
        ret.append((cond,cons))
        #print(cond,cons,self.cur_tok)
        while(str(self.cur_tok)==TTELIF):
            self.advance()
            self.tot+=1
            cond = self.cmp()
            if str(self.cur_tok) != TTTHEN: 
                self.tot+=MAKEPERROR
                return ret
            self.advance()
            self.tot+=1
            cons = self.cmp()
            ret.append((cond,cons))
        if(str(self.cur_tok)==TTELSE):
            self.advance()
            self.tot+=1
            cons= self.cmp()
            ret.append((NumberNode(Token(TT_INT,1)),cons))
        return UnaryOpNode(TTIF,ret)

    def makewhile(self):
        self.advance()
        ret=[]
        cond = self.cmp()
        if str(self.cur_tok) not in (TTTHEN): 
            self.tot+=MAKEPERROR
            return ret
        self.advance()
        self.tot+=1
        cons = self.cmp()
        ret=(cond,cons)
        return UnaryOpNode(TTWHILE,ret)

    def factor(self):
        self.tot+=1
        tok=self.cur_tok

        if tok.type in (TTPLUS,TTMINUS,TTNOT):
            self.advance()
            factor= self.factor()
            return UnaryOpNode(tok,factor)
        elif tok.type in (TT_INT,TTIDENTIFIER): 
            self.advance()
            return NumberNode(tok)
        elif tok.type in (TTLPAREN):
            self.advance()
            expr = self.cmp()
            if self.cur_tok.type in (TTRPAREN):
                self.tot+=1
                self.advance()
                return expr
            else: self.tot+=len(self.tokens)
        elif tok.type in (TTLBRACE):
            self.advance()
            multiexpr= self.statements()
            if self.cur_tok.type in (TTRBRACE):
                self.tot+=1
                self.advance()
                return multiexpr
            return multiexpr
        elif tok.type in(TTIF):
            return self.makeifcond()
        elif tok.type in(TTWHILE):
            return self.makewhile()
        elif tok.type in (TTINPUT,TTOUTPUT):
            self.advance()
            if(self.cur_tok.type != TTIDENTIFIER):
                print("Only input single variables")
                self.tot+=MAKEPERROR
                self.advance()
                return
            else:
                val=self.cur_tok
                self.tot+=1
                self.advance()
                return UnaryOpNode(tok,val)
    def term(self):
        return self.ops(self.factor,(TTMUL,TTDIV))
    def expression(self):
        #print(self.cur_tok.type)
        if str(self.cur_tok.type) in (TTVAR):  ######################################### MADE CHANGES
            self.advance()
            self.tot+=1
            id=self.cur_tok
            #self.op_tok
            if self.cur_tok.type != TTIDENTIFIER:
                self.tot+=len(self.tokens) #ERROR
            else:
                self.advance()
                self.tot+=1
                if(self.cur_tok.type!= TTEQ):
                    self.tot+=len(self.tokens)#ERROR
                else: 
                    self.advance()
                    self.tot+=1 
                    return BinOpNode(NumberNode(id,True),TTEQ,self.expression())
        return self.ops(self.term,(TTPLUS,TTMINUS,TTEQ,TTAND,TTOR))
    def cmp(self):
        ret = self.ops(self.expression,(TTEE,TTGT,TTGTE,TTLT,TTLTE,TTNE))

        # if self.cur_tok.type == TTNEWLINE:
        #     self.advance()
        #     self.tot+=1
        # else:
        #     self.tot+=MAKEPERROR
        return ret
    def ops(self,func,op):
        left =func()
        #print(self.cur_tok)
        while(self.cur_tok.type in op):
            self.tot+=1
            op_tok = self.cur_tok
            self.advance()
            right = func()
            left = BinOpNode(left,op_tok,right)
            
        return left        

    def statements(self):
        #print("IN statements")
        ret= []
        while(self.idx<len(self.tokens) and self.cur_tok.type != TTRBRACE):
            ret.append(self.cmp())
            if(self.cur_tok.type==TTNEWLINE):
                self.tot+=1
                self.advance()
            else :
               # print("SEMICOLON",self.cur_tok.type)
                self.tot+=MAKEPERROR
                return ret
        return ret




#####################################################

#####################################################

zura = SymbolTable()

def run(text):
    #print(type(text),text)
    lex = Lexer(text)
    tokens = lex.make_token()
    #print(LETTERS)
    #print("OK",tokens)
    if(type(tokens)==str): return tokens
    #print("LEXICAL A OK")
    #print("After Tokenization: ",tokens)
    parser = Parser(tokens)
    tree = parser.pasrse()
    #print(parser.tot,len(tokens))
    #print(tree)
    if(not tokens or parser.tot!= len(tokens)): 
        print("INVALID EXPRESSION")
        return
    #return interpretter(tree,zura)
    

    intercode=[]
    ## code generation
    #print(tree)
    code_generator(tree)
    return "OK"
