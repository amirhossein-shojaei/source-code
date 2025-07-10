#Display the name, surname, and age of the inheritance class.

class waled:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def distroy(self):
        print(self.fname, self.lname)

class person(waled):
    def __init__(self,fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def destroy(self):
        super().distroy()
        print(self.age)
str1 = person('amirhossein', 'shojaei', 18)
str1.destroy()