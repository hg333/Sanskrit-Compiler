class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent =None
        self.cur=0
    def get(self, name):
        
        if isinstance(name,int) : return name
        if isinstance(name,list): return name

        if(not self.available(name)):
            SystemExit("Undeclared Variable "+ name)
        value=self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value
    def set(self, name,value):
        self.symbols[name]=value
    def remove(self,name):
        del self.symbols[name]
    def available(self,name):
        return name in self.symbols