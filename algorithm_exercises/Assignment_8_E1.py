# ISI 300  Vincenzo Mezzio      Assignment 8
# Tree Traversal
# Exercise 1 Pre-order

# Assume each node has at the most two children, left sub tree and right sub tree

# Middle - Left - Right -> 10, 5, 2, 8, 15, 12

class Node: # this is a class, represents every single Node in the tree
    # initialize the tree: one ROOT, empty subtrees
    def __init__(self, data): # sets data the node contains, no branches
        self.left = None
        self.right = None
        self.data = data
        
    def display_info(self):
        print("Value in Node:",self.data) # displaying node
        print("Left Branch:", self.left)
        print("Right Branch:", self.right)
        
    # insert data in the left sub-tree
    # May not be the most efficient way to do this
    def insert_left(self, data):
        self.left = Node(data)
        
    # insert data in the right sub-tree
    def insert_right(self, data):
        self.right = Node(data)
        
    # Print the tree
    def visit_preorder(self): 
        ##pre order: middle, left, right
        print(self.data) #print root
        if self.left is not None: # if there is a left sub tree, go in it and print again
            self.left.visit_preorder() # fcn calling same fcn again (recursion )
            
        if self.right is not None:
            self.right.visit_preorder()
        ## my function ends

    
    
a_node = Node('10')

a_node.insert_left("5") 

a_node.insert_right("15") 

a_node.left.insert_left("2") 

a_node.left.insert_right("8") 

a_node.right.insert_left("12") 

print()
print("Print tree")
a_node.visit_preorder() 

    