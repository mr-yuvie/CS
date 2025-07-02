# You can't insert and delete in an array.
# Singley Linked List- You can't go back [A->B->C->D]
# How to Insert into a Linked List? Break prev ties and creat new ties.
# How to Delete(C) in a Linked List? Break the next node and point B to D then delete D->C and point it to B
# C.prev = C.next = Null
# Deletion & Insertion: O(1) [not for ending values]
# To get a value we have to walk the list node by node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printing_linked_list():
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")


# Creating Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
head = node1

# Connecting Nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Printing the linked list
printing_linked_list()

# Adding a new Node at the beginning
node0 = Node(00)
node0.next = node1
head = node0

# Printing the linked list
printing_linked_list()

# Adding a new Node at the end
node5 = Node(50)
node4.next = node5

# Printing the linked list
printing_linked_list()

# Adding a new Node at a specific position
new_node = Node(25)
current = head
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

# Printing the linked list
printing_linked_list()

# Deletion from the beginning
if head is not None:
    head = head.next  # Update the head to next node

# Printing the linked list
printing_linked_list()

# Deletion from the end
current = head
while current.next.next is not None:
    current = current.next
current.next = None

# Printing the linked list
printing_linked_list()

# Deleting a Particular Node
current = head
while current.next.data != 25:
    current = current.next
current.next = current.next.next

# Printing the linked list
printing_linked_list()
