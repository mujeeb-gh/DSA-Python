# similar to a dictionary

head = {
  'value': 11,
  'next': {
    'value': 3,
    'next': {
      'value': 23,
      'next': {
        'value': 7,
        'next': None
      }
    }
  }
}

# print(head['next']['next']['value'])

# LL Constructor
class Node:
  def __init__(self, value):
    self.value= value
    self.next = None
    

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
    
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
      
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return
    
  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -=1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp.value
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp
  
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp
  
  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
    
    # if index < 0 or index >= self.length:
    #   return None
    # temp = self.head
    # for _ in range(index):
    #   temp = temp.next
    # temp.value = value
    # return 
  
  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True     
  
  def remove(self, index):
    if index < 0 or index > self.length:
      return None
    if index == 0:
      self.pop_first()
    if index == self.length - 1:
      self.pop()
    prev = self.get(index - 1)
    # temp = self.get(index) # this would work but it is O(n), and there's a O(1) alternative
    temp = prev.next # this is the O(n) alternative
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp
  
  def reverse(self): # Very common interview question
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
      
  # Exercises
  # Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
  def find_middle_node(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
    
    
    
    
      
      

    
  
my_linked_list= LinkedList(4)
# my_linked_list.append(45)
my_linked_list.append(90)
my_linked_list.prepend(23)
my_linked_list.prepend(12)
# my_linked_list.pop_first()

my_linked_list.set_value(1, 460)
my_linked_list.insert(1, 20)
my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.find_middle_node()

# my_linked_list.pop()
my_linked_list.print_list()
print(f'\n\nLinked List length: {my_linked_list.length}')
