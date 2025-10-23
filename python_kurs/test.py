class Person:
    __alter = 42
    
    def getAlter(self):
        return self.__alter

obj = Person()
print(obj.getAlter())
