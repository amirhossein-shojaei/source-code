#Deleting a name from a database in object-oriented programming

class student:
    
    db= []
    def __init__(self , name , lname , age):
        self.name = name
        self.lname = lname
        self.age = age
        self.db.append(self.name)
    
    def __del__(self):
        self.db.remove(self.name)
    
    def sleep(self):
        return f"{self.name} is sleeping!"

Hossein = student('hossein','musavi',20)
Amir = student('amir','molaei',20)
Ali = student('ali','shojaei',20)
Arman = student('arman','mohamadi',18)
del Arman
del Hossein
print(Ali.db)