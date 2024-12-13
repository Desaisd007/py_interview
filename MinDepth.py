# Height of Binary Tree(Min Depth)

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def min_height_tree(A):
    if( A == None):
        return 0
    else:
        ldepth = min_height_tree(A.left)
        rdepth = min_height_tree(A.right)
        if(ldepth>rdepth):
            return (1+rdepth)
        else:
            return (1+ldepth)



root = Node(1)
root.left =Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(7)
root.right.right=Node(6)

print(min_height_tree(root))
