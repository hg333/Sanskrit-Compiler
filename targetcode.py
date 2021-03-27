

import sys

original_stdout = sys.stdout # Save a reference to the original standard output
f= open('text.asm', 'w')
sys.stdout = f


tac = open("tac.txt",'r')

t1="t1"
t2="t2"
t3="t3"
a0="a0"
v0 = "v0"

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.cur=0
    def get(self, name):
        
        if isinstance(name,int) : return name
        if(not self.available(name)):
            SystemExit("Undeclared Variable "+ name)
        value=self.symbols.get(name, None)
        return value
    def set(self, name):
        if self.available(name): return

        self.symbols[name]=self.cur+4
        self.cur+=4
    def remove(self,name):
        del self.symbols[name]
    def available(self,name):
        return name in self.symbols
print("main:")
print('add $sp, $sp, -400')
addresstable = SymbolTable()

def load(register,val):
    global addresstable

    try: 
        numeric = int(val)
        print(f'li ${register}, {numeric}') 
    except:
        temp=400-addresstable.get(val)
        print(f'lw ${register},{temp} ($sp)')

def save(register,val):
    global addresstable
    temp=400-addresstable.get(val)
    print(f'sw ${register},{temp} ($sp)')


count = 1

def normalize(register):
    global count
    print(f'move $t4, ${register}')
    print(f'li ${register}, 1')
    print(f'bne $t4, 0, yareyare{count}') # changed from bgt to bne
    print(f'li ${register}, 0')
    print(f'yareyare{count}:')
    count+=1

for code in tac:
    code = code.strip()
    v=code.split(' ')
    #print(v)
    if(len(v)==0): continue
    if(len(v)==1):
        print(f'{v[0]}:')
    elif len(v)==2:
        if(v[0]=="input"):
            print("li $v0, 5")
            print("syscall")
            save(v0,v[1])
        elif v[0]=='output':
            print("li $v0, 1")
            load(a0,v[1])
            print('syscall')
        elif v[0] =='goto':
            print(f" b {v[1]}")
        else:
            print('$$$',v,"$$$")
    elif len(v) ==3: #assignment 
        try:
            val = int(v[2])
            addresstable.set(v[0])
            print(f'li $t1, {v[2]}')
            save(t1,v[0])
        except:
            val = v[2]
            load(t1,val)
            addresstable.set(v[0])
            print(f'move $t2, $t1')
            save(t2,v[0])
    elif len(v)==4: # if statement 
        if(v[0]=="IFNOT"):
            load(t1,v[1])
            normalize(t1)
            print(f'bne $t1, 1, {v[3]}')
        elif v[0]=="IF":
            load(t1,v[1])
            normalize(t1)
            print(f'beq $t1, 1, {v[3]}')
        elif v[2]== '!': 
            load(t1,v[3])
            normalize(t1)
            print("li $t2 1")
            print("sub $t3, $t2, $t1")
            save(v[0],t3)
        else : pass
    elif len(v) ==5: #operation
        op = v[3]
        addresstable.set(v[0])
        if v[3] == '+':
            load(t1,v[2])
            load(t2,v[4])
            print(f'add $t3, $t1, $t2')
            save(t3,v[0])
        elif v[3]=='-':
            load(t1,v[2])
            load(t2,v[4])
            print(f'sub $t3, $t1, $t2')
            save(t3,v[0])
        elif v[3]=='*':
            load(t1,v[2])
            load(t2,v[4])
            print(f'mult $t1, $t2')
            print("mflo $t3")
            save(t3,v[0])
        elif v[3]=='/':
            load(t1,v[2])
            load(t2,v[4])
            print(f'div $t1, $t2')
            print("mflo $t3")
            save(t3,v[0])
        elif v[3]=='>':
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"ble $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        elif v[3]=='<': 
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"bge $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        elif v[3]=='>=': 
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"blt $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        elif v[3]== '<=':
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"bgt $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        elif v[3] == '==':
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"bne $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        elif v[3] == '!=':
            load(t1,v[2])
            load(t2,v[4])
            print("li $t3, 0")
            print(f"beq $t1, $t2 ,yareyare{count}")
            print("li $t3, 1")
            print(f'yareyare{count}:')
            save(t3,v[0])
            count+=1
        
    else:
        print(f'###{code}###')

print("li $v0, 10")
print("syscall")