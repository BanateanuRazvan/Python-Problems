
class Graph:
    def __init__(self):
        self.list = {}
        self.number = 0

    def addVortex(self,value):
        self.list[value]=[]
        self.number+=1

    def addLinks(self,value1,value2):
        self.list[value1].append(value2)
        self.list[value2].append(value1)

a=Graph()
a.addVortex(5)
a.addVortex(6)
a.addVortex(7)
a.addVortex(8)
a.addLinks(5,6)
a.addLinks(5,8)
a.addLinks(8,7)


print(a.list)