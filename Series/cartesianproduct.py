resource_type = 'mssql'
type = 'parentnode'


class MantaNodes:
    node_ids = [1, 2, 3]
    node_parent_ids = [1000, 2000, 3000]
    node_names = ['node1', 'node2', 'node3']

    def __init__(self):
        self._nodes = [Node(id,parent_id,str) for id in self.node_ids for parent_id in self.node_parent_ids for name in self.node_names]

    def __len__(self):
        return len(self._nodes)



class Node:
    def __init__(self,id,parent_id,name):
        self.id = id
        self.parent_id = parent_id
        self.name = name

    def __repr__(self):
        return 'Node Object:id={},parent_id={},str ={}'.format(self.id,self.parent_id,self.str)


class ParentNode:
    def __init__(self,id,parent_id,str,resource_type):
        self.id = id
        self.parent_id = parent_id
        self.type = type
        self.resource_type = resource_type

    def __repr__(self):
        return 'Parent Node: id={}, parent_id={},type={},resource_type={}'.format(self.id,self.parent_id,self.type,self.resource_type)


#instatiating node objects
node1 = Node(1,1000,'node1')
node2 = Node(2,2000,'node2')
node3 = Node(3,3000,'node3')

#instatiating parent objects
parentnode1 = ParentNode(1000,None,type,resource_type )
parentnode2 = ParentNode(2000,None,type,resource_type)
parentnode3 = ParentNode(3000,None,type,resource_type)



# tuples of instantiated objects
parent_nodes = (parentnode1,parentnode2,parentnode3)
nodes = (node1,node2,node3)


#using list comprehension to create a cartesian product: every combination of nodes + parent_nodes
nodes_and_parents = [(parent_nodes,nodes) for node in nodes for parent in parent_nodes]


#########
#Trying to instatiate objects based on a list
#########


node_id_attributes = [1,2,3]
node_parent_id_attributes = [1000,2000,3000]
node_str_attributes = ['node1','node2','node3']

manta_nodes = MantaNodes()
len(manta_nodes)