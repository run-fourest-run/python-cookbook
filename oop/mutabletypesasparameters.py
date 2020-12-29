'''
Mutable types in parameters are a bad idea...

optional parameters with a default value are a great feature of Python


'''



class Nodes:
    def __init__(self,node=None):
        if self.node is None:
            self.node = []
        else:
            self.node = list(node)

    def __add__(self, other):
        pass


    def __repr__(self):
        classname = type(self).__name__
        print('{}({!r}'.format(classname,self.node))



class FuckedNodes:
    def __init__(self,nodes = []):
        self.nodes = nodes


    def pick(self,node):
        self.nodes.append(node)


    def __repr__(self):
        classname = type(self).__name__
        ("{}({!r})".format(classname,self.nodes))

nodes = ['node1','node2']
fuckednodes1 = FuckedNodes(nodes)
print(fuckednodes1.nodes)
fuckednodes2 = FuckedNodes()