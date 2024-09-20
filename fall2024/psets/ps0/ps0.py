#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v: BTvertex):
    # base case
    if (v == None): return 0

    # the +1 includes the node itself
    s = calculate_sizes(v.right) + calculate_sizes(v.left) + 1

    v.size = s
    return s

#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    if (v.size >= t and v.size <= (2 * t)):
        return v
    
    else:
        if (v.left != None):
            w = FindDescendantOfSize(t, v.left)
            if w != None: return w
        if (v.right != None):
            w = FindDescendantOfSize(t, v.right)
            if w != None: return w
            
    return None