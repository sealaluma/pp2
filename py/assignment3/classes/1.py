class strings():
    def __init__(self):
        self.str = ""
    
    def getString(self):
        self.str = input()
    
    def printString(self):
        print(self.str.upper())
        
        
str = strings()
str.getString()
str.printString()