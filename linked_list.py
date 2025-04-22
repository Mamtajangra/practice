# define a node 
class Node:
    # it is a constuctor having data 
    def __init__(self,data):
        # features of class 
        self.data = data 
        self.next = None
    
# define linked list 
class Linked_list:
    # define constructor 
    def __init__(self,head = None):
        self.head = head 
    
    # traversing print all values 
    def traverse(self):
        # temp is pointer instruct head
        temp = self.head 
        # loop upto obtain none 
        while temp:
            # print temp.data 
            print(temp.data,end="--->")
            # for next value 
            temp = temp.next
        print(None)

    # insert values in above linked list 
    def insert(self,value):
        # it creates new node 
        new_node = Node(value)
        # for next node linked 
        new_node.next = self.head
        # add head to new node 
        self.head = new_node


# obtain node 
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# let head = n1 
head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# LL1 is linked list 
LL1 = Linked_list(head)
# traversing before adding new node 
LL1.traverse()
LL1.insert(90)
LL1.insert(100)
LL1.insert(110)
LL1.insert(120)
LL1.insert(130)
LL1.insert(140)


print("after insertion at beginning")

# traversing after adding new node 
LL1.traverse()





