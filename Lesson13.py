class Stundent:

    def __init__(self,name):
        self.name = name

    def avg(self,math,english):
        print((math + english)/2)

a001 = Stundent("sato")
# a001.avg(30,70)

# a001.name = "sato"
print(a001.name)

a002 = Stundent("tanaka")
# a002.name = "tanaka"
print(a002.name)