class Node:
    def __init__(self, id, label, parent, children):
        self.id = id
        self.label = label
        self.parent = parent 
        self.children = children
# define a class to describe attributes of node
# here id is the unique value for each node; label is contents of each node. e.g. "a", "b"
# parent/ children: is to build tree

Nodes = [] # save nodes in a list
count_id = 1 # at first, count_id = 1 corresponds to root node
root = Node(id=0, label = "", parent=-1, children=[]) 
Nodes.append(root)

# this function is used to find nodes by id
def SearchNode(n):
    for i in Nodes:
        if i.id == n:
            return i
    return None


def build(s):
    global count_id 
    current_id = 0 # every time we handle with a new input word, we search from the root node
    for i in s: 
        current_node = SearchNode(current_id)
        flag = 0 # use flag to value to represent whether children of current node match the label
        for j in current_node.children:
            child = SearchNode(j)   # find children and judge
            if child.label == i:    
                current_id = child.id # jump to next id/ node
                flag = 1
                break
        if not flag:    # when no children match to this label
           new_Node = Node(id=count_id, label=i, parent=current_id,children=[]) # generate a new node and append
           Nodes.append(new_Node) 
           current_node.children.append(new_Node.id)
           count_id += 1
           current_id = new_Node.id # jump to the new node

build("apple")
build("applaaa")
print("end")