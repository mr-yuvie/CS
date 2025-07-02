# Doubley Linked List- You can go back [A<->B<->C<->D]
# Not Completed Yet
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def printing_linked_list_next():
    current = head
    while current is not None:
        print(current.data, end="<->")
        current = current.next
    print("None")


def printing_linked_list_prev():
    current = tail
    while current is not None:
        print(current.data, end="<->")
        current = current.prev
    print("None")


# Creating Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
head = node1
tail = node4

# Connecting Nodes
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Printing the linked list
printing_linked_list_next()
printing_linked_list_prev()

# Adding a new Node at the beginning
node0 = Node(00)
node0.next = node1
head = node0

# Printing the linked list
# printing_linked_list()

# Adding a new Node at the end
node5 = Node(50)
node4.next = node5

# Printing the linked list
# printing_linked_list()

# Adding a new Node at a specific position
new_node = Node(25)
current = head
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

# Printing the linked list
# printing_linked_list()

# Deletion from the beginning
if head is not None:
    head = head.next  # Update the head to next node

# Printing the linked list
# printing_linked_list()

# Deletion from the end
current = head
while current.next.next is not None:
    current = current.next
current.next = None

# Printing the linked list
# printing_linked_list()

# Deleting a Particular Node
current = head
while current.next.data != 25:
    current = current.next
current.next = current.next.next

# Printing the linked list
# printing_linked_list()
