#Construct a full binary tree using preorder and mirror preorder traversals

class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
 
# A utility function to print inorder
# traversal of a Binary Tree
def prInorder(node):
    if (node == None) :
        return
    prInorder(node.left)
    print(node.data, end = " ")
    prInorder(node.right)
 
# A recursive function to construct Full 
# binary tree from pre[] and preM[].
# preIndex is used to keep track of index
# in pre[]. l is low index and h is high
# index for the current subarray in preM[]
def constructBinaryTreeUtil(pre, preM, preIndex,
                                    l, h, size):
    # Base case
    if (preIndex >= size or l > h) :
        return None , preIndex
 
    # The first node in preorder traversal 
    # is root. So take the node at preIndex
    # from preorder and make it root, and
    # increment preIndex
    root = newNode(pre[preIndex])
    preIndex += 1
 
    # If the current subarray has only
    # one element, no need to recur
    if (l == h):
        return root, preIndex
 
    # Search the next element of
    # pre[] in preM[]
    i = 0
    for i in range(l, h + 1):
        if (pre[preIndex] == preM[i]):
                break
 
    # construct left and right subtrees
    # recursively
    if (i <= h):
 
        root.left, preIndex = constructBinaryTreeUtil(pre, preM, preIndex,
                                                               i, h, size)
        root.right, preIndex = constructBinaryTreeUtil(pre, preM, preIndex,
                                                       l + 1, i - 1, size)
 
    # return root
    return root, preIndex
 
# function to construct full binary tree
# using its preorder traversal and preorder
# traversal of its mirror tree
def constructBinaryTree(root, pre, preMirror, size):
 
    preIndex = 0
    preMIndex = 0
 
    root, x = constructBinaryTreeUtil(pre, preMirror, preIndex,
                                             0, size - 1, size)
 
    prInorder(root)
 
# Driver code
if __name__ =="__main__":
 
    preOrder = [1, 2, 4, 5, 3, 6, 7]
    preOrderMirror = [1, 3, 7, 6, 2, 5, 4]
 
    size = 7
    root = newNode(0)
 
    constructBinaryTree(root, preOrder,
                        preOrderMirror, size)
 
