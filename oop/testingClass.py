from array import array


class Node:

    typecode = 'd'

    def __init__(self, node_id, parent_id, resource, layer):
        self.node_id = float(node_id)
        self.parent_id = float(parent_id)
        self.resource = resource
        self.layer = layer

    def __iter__(self):
        return (i for i in (self.node_id, self.parent_id, self.resource, self.layer))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r},{!r},{!r})'.format(class_name,*self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    @classmethod
    def from_bytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


node1 = Node('1','123','mssql','layer1')
print(node1)
for x in node1:
    print(x)


