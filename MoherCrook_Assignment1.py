# Casey Moher-Crook
# Assignment 1
# Github username: ccrook3

# Part 1: Queue
# Wasn't sure how else to do this one with the python queue module
# So I just wrapped "my own" queue around it.
import Queue

class MyQueue(object):
	# Create a python queue object from the queue module
    def __init__(self):
        self.q = Queue.Queue()

    def myPut(self, value):
        if self.q.full() == False:
            self.q.put(value)
        else:
            print "Queue Full."
    
    def myGet(self):
        return self.q.get()

# Part 2: Stack
class MyStack(object):
    # Initialize the stack as a list
    def __init__(self):
        self.size = 0
        self.Stack = []
    
    # Add new numbers to the end of the list
    def push(self, number):
        self.Stack.append(number)

    # Delete numbers from the end of the list
    def pop(self):
        ret = self.Stack.pop()
        return ret

    def checkSize(self):
        return len(self.Stack)

    def showStack(self):
        print self.Stack


# Part 3: Binary Tree

class BinTree(object):
    # To create a binary tree, specify the left and right nodes,
    # the key, and the parent node. If no parent node, put None
    def __init__(self, value, parentValue):
        self.left = None
        self.right = None
        self.key = value
        self.parent = parentValue
    
    # Small helper function to see if the node is childless
    def has_children(self, key):
        if self.left == None and self.right == None:
            return False
        else:
            return True
    
    # This function is used to find a node in the tree.
    # Because the tree is unsorted, we have to recursively look
    # through every node.
    def lookup(self, value):
        if self.key == value or self == None:
            return self
        else:
            # Here, we look through both the left and right children
            if self.left != None:
                if self.left.lookup(value) != None:
                    return self.left.lookup(value)
            if self.right != None:
                if self.right.lookup(value) != None:
                    return self.right.lookup(value)


    def add(self, value, parentValue):
        # First, look up the node in the tree and make sure that its
        # parent exists
        temp = BinTree(0, None)
        temp = self.lookup(parentValue)
        if temp == None:
            print "Parent not found."
        else:
            # Add to left first, then right if left is full.
            if temp.left == None:
                temp.left = BinTree(value, temp)
            elif temp.right == None:
                temp.right = BinTree(value, temp)
            else:
                print "Parent has two children, node not added."

    def delete(self, value):
        # First, look up the node using its value
        temp = BinTree(0, None)
        temp = self.lookup(value)
        if temp == None:
            print "Node not found."
        elif temp.has_children(temp.key):
            print "Node not deleted, has children."
        else:
            # If the node is it's parent's right child, delete it
            # if not, delete the left child
            if temp.parent.right == temp:
                temp.parent.right = None
            else:
                temp.parent.left = None
        
    # Print the parent and then the two children, if they aren't null
    def binPrint(self):
        if self != None:
            print self.key
            if self.left != None:
                self.left.binPrint()
            if self.right != None:
                self.right.binPrint()
        else:
            return


# Part 4: Graph

class MyGraph(object):
    def __init__(self):
        self.theGraph = {}
    
    def addVertex(self, value):
        if value not in self.theGraph.keys():
            self.theGraph[value] = []
        else:
            print "Vertex already exists."

    def addEdge(self, vert1, vert2):
        # Make sure that both vertices are in the dictionary
        if (self.theGraph.has_key(vert1)) and (self.theGraph.has_key(vert2)):
            self.theGraph[vert1].append(vert2)
            self.theGraph[vert2].append(vert1)
        else:
            print "One or both vertices not found."

    
    def findVertex(self, value):
        if value in self.theGraph.keys():
            print self.theGraph[value]

# Part 5: Testing

# a. MyQueue
# put 10 consecutive numbers into the queue
print "Queue Tests:"
q = MyQueue()
for i in range (0,10):
    q.myPut(i)
# pop all the numbers in the queue
for i in range (0,10):
    print q.myGet()


print


# b. MyStack
print "Stack Tests:"
# Add 10 numbers to the stack
m = MyStack()
for i in range (1,11):
    m.push(i)
# Pop 10 numbers from the stack
for i in range (1,11):
    print m.pop()

print

# c. BinTree
print "Binary Tree Tests:"
# Here, create the tree and add any numbers so that they don't break the
# bintree rules.
t = BinTree(20, None)
t.add(10,20)
t.add(30,20)
t.add(5,10)
t.add(7,10)
t.add(45,30)
t.add(25,30)
t.add(50,45)
t.add(70,50)
t.binPrint()
t.delete(7)
t.delete(70)
print "After Deletions:"
t.binPrint()

print

# d. Graph
print "Graph Tests:"
g = MyGraph()
# add some vertices
for i in range(1,11):
    g.addVertex(i)
x = 1
y = 2
# add a lot of edges
while y < 10:
    g.addEdge(x,y)
    x = x + 1
    y = y + 1
x = 1
y = 4
# add a lot more edges
while y < 10:
    g.addEdge(x,y)
    x = x + 1
    y = y + 1
# find all the vertices to get their edges.
for i in range(1,11):
    g.findVertex(i)
