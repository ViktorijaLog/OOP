class person:
    def set(self,name,age):
        self.name= name
        self.age= age
    def output (self):
        print(f'Persona {self.name}, kurai ir {self.age} gadi')

p = person()
p.set("Peter",20)
p.output()



p = person()
p.set("Viktorija",17)
p.output()