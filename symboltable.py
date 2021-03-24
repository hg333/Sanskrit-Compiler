class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent =None
    def get(self, name):
        
        if isinstance(name,int) : return name
        if isinstance(name,list): return name
        value=self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value
    def set(self, name,value):
        self.symbols[name]=value
    def remove(self,name):
        del self.symbols[name]
    def available(self,name):
        self.symbols.__contains__(name)