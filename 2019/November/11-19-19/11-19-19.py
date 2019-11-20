'''
DAILY CODING CHALLENGE

DATE: 11/19/19

CHALLENGE: A unival tree (which stands for "universal value") is a tree where all
           nodes under it have the same value. Given the root to a binary tree,
           count the number of unival subtrees.

           E.G.: The following tree has 5 unival subtrees [(0),(1),(1),(1),(1,1,1)]:

                  0
                 / \
                /   \
               /     \
              1       0
                     / \
                    /   \
                   1     0
                  / \
                 1   1
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left  = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            elif value == self.value:
                if self.right is None and self.left is None:
                    self.right = Node(value)
                    self.left  = Node(value)
                else:
                    self.right.insert(value)
                    self.left.insert(value)
        else:
            self.value = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value),
        if self.right:
            self.right.printTree()

def isUnival(root):
    if root == None: return True
    if root.left != None and root.left.value != root.value: return False
    if root.right != None and root.right.value != root.value: return False
    if isUnival(root.left) and isUnival(root.right): return True
    return False

def countUnivals(root):
    if root == None: return (0, True)

    leftCount, leftUnival = countUnivals(root.left)
    rightCount, rightUnival = countUnivals(root.right)
    isUnival = True

    if not leftUnival or not rightUnival: isUnival = False
    if root.left != None and root.left.value != root.value: isUnival = False
    if root.right != None and root.right.value != root.value: isUnival = False
    if isUnival: return (leftCount + rightCount + 1, True)
    else: return (leftCount + rightCount, False)

def helper(root):
    count, isUnival = countUnivals(root)
    return count


'''
TESTING

BREAKDOWN: Creates a BNS, traverses the BNS and returns the Unival count.
           For this test, I have created the following BNS:

             2
            / \
           /   \
          /     \
         /       \
        1         4
       / \       / \
      /   \     /   \
     /     \   /     \
    1       1 3       5
                     / \
                    /   \
                   5     5
                  / \   / \
                 5   5 5   5
'''

tree = Node(2)
tree.insert(1)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(5)
tree.insert(5)

expected = 11
actual   = helper(tree)
passed   = False

if expected == actual: passed = True

print("\n---UNIVAL SUBTREE TEST---")
tree.printTree()

print("\nEXPECTED: {}".format(expected))
print("ACTUAL:   {}".format(actual))
print("PASSED:   {}".format(passed))
print("-------------------------\n")
