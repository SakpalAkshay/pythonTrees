class BinaryTreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        #A  class for creating Tree Nodes
        

#lets create some nodes

rootNode = BinaryTreeNode(1)
leftNode = BinaryTreeNode(2)
rightNode = BinaryTreeNode(3)

leftNodeLeftNode = BinaryTreeNode(4)
leftNodeRightNode = BinaryTreeNode(5)

rightNodeLeftNode = BinaryTreeNode(6)

#lets create some connections

rootNode.left = leftNode
rootNode.right = rightNode

leftNode.left = leftNodeLeftNode
leftNode.right = leftNodeRightNode

rightNode.left = rightNodeLeftNode

# As now connections are done we need to print them
#We shall use recusion to print our tree
'''#Note every root node will have two subtree 
and every subtree will have a root, which will eventually have two subtree,
only exception our nodes pointing to NONE'''

def printTree(root):
    '''Base case would be if root is None, 
    i.e Tree is empty then return nothing, else print the root
    '''
    if root is None:
        return
    
    print(root.data, end=":")
    
    #Now we will only print left or right node if its not none
    #this is another one of the conditions
    
    if root.left != None:
        print("L=> ", root.left.data, end = ",") #this prints the data in left node
    
    if root.right !=None:
        print("R=> ", root.right.data, end=",") #this prints data in right node
    
    print()
    
    printTree(root.left) #switching to the left subtree 
    printTree(root.right) #swithcing to the right subtree
    
#lets call it
printTree(rootNode)
