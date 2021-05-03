# ISI 300   4/12/21
# Trees

# CS view of a tree looks at it upside down
#           Root
#          /    \
#         Branches
#        /        \
#      Leaf      Leaf


# define a Node (for a Tree)
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
    def print_tree(self):  ## <-- B then D, E, F
        ## can be any operation
        ## for us just a simple printout
        ## can be a complicated function
        print("Value is",self.data),
        if self.left is not None: # if there is a left sub tree, go in it and print again
            print("stepping in left tree")
            self.left.print_tree() # fcn calling same fcn again (recursion )
            
        if self.right is not None:
            print("stepping in left tree") # may get confusing with longer trees to display which side we are stepping into
            self.right.print_tree()
        ## my function ends
        ## go back to D (from E) B (from D) F (from B)
    
    
a_node = Node('A')

print()
print("root only, info for A")

a_node.display_info()

print()
print("add B as a child to A, on left branch")
a_node.insert_left("B") # B will be converted as a node and attached to the left

print()
print("Display updated info for A")
a_node.display_info() # will print out B as a location in memory rather than B

print()
print("Print tree rooted at A")
a_node.print_tree()

print()
print("add C as a child to A, on right branch")
a_node.insert_right("C")

print()
print("Print tree rooted at A (second call)")
a_node.print_tree()


