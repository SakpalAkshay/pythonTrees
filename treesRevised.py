class BinaryTreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None #Left and Right Children of the tree initialized as None
        
        
n1 = BinaryTreeNode(0)
n2 = BinaryTreeNode(1)
n3 = BinaryTreeNode(3)

n1.left = n2
n1.right = n3

if(n1.right.data == n3.data): # different ways of accessing data
    print("Comparision True")
else:
    print("Comparision False")
    
    
    
def printTree(root): #this will be based on recursion and would traverse our in Pre Order (Root->Left->Right)
    #base condition
    
    if root is None:
        return

    print(root.data,":", end=" ")
    if root.left is not None:
        print("L => ", root.left.data, end=',')
    
    if root.right is not None:
        print("R => ", root.right.data, end= ",")
    print()
    
    printTree(root.left)
    printTree(root.right)
    
    
    
def countTreeNodes(root):
    
    if root is None:
        return 0 
    
    left = countTreeNodes(root.left)
    right = countTreeNodes(root.right)
    
    return left + right + 1
    
printTree(n1)
count = countTreeNodes(n1)
print(count)


def takeInput():
    
    root = int(input())
    
    #termination condition is that if root is -1 than we return None
    
    if root == -1:
        return None
    
    rootNode = BinaryTreeNode(root)
    
    #lets build the left subtree
    leftTree = takeInput() #individuals nodes will get created and connected recursively
    rightTree = takeInput()
    
    
    #lets connect our left and Right childs
    
    rootNode.left = leftTree
    rootNode.right = rightTree
    
    return rootNode


root = takeInput()
printTree(root)
