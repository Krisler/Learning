class Node:
  def __init__(self, data=None):
    self.data = data # Stores data
    self.next = None # pointer to the next node

class LinkedList:
  def __init__(self):
    self.head = None
  
  # Traversing the list
  def traverse_list(head):
    current = head
    while current:
      print(current.data)
      current = current.next

  def insert_at_beginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  #Insertion at the Beginning
  def insert_at_beginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  # Insertion at the End
  def insert_at_end(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node
  
  # Insertion After a Given Node:
  def insert_after(self, prev_node, new_data):
    if prev_node is None:
        print("Previous node must exist.")
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

# Deletion at the End
  def delete_at_beginning(self):
    if self.head is None:
      return
    self.head = self.head.next

# Delete at the End
  def delete_at_end(self):
    if self.head is None:
      return
    if self.head.next is None:
      self.head = None
      return
    second_last = self.head
    while second_last.next.next:
      second_last = second_last.next
    second_last.next = None

# Deletion by Value
  def delet_node(self, key):
    temp = self.head
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        return
    
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    if temp is None:
      return
    prev.next =temp.next
    
def search(self, key):
    current = self.head
    while current is not None:
        if current.data == key:
            return True
        current = current.next
    return False

# Creating a linked list with nodes 1 -> 2 -> 3
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second  # Link first node to second
second.next = third    # Link second node to third