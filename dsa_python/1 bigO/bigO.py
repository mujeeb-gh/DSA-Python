# O(n) Linear Complexity -- Runtime directly proportional to size of input "n"

def print_items(n):
  for i in range(n):
    print(i)
    
# print_items(16)

# Drop Constants for Simplicity
# O(2n) == O(n) --> Same as Linear Time Complexity
def print_items(n):
  for i in range(n):
    print(i)
  for j in range(n):
    print(j)

# O(n^2) --> Quadratic Time Complexity
# O(n^k)== O(n^2) where k = 2,3,4...n
def print_items(n):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        print(i, j,k)
        
# Drop non-dominants --> O(n^2) is dominant, therefore O(n) is dropped, and The function is still running in Quadratic Time O(n^2)
def print_items(n):
  # O(n^2)
  for i in range(n):
    for j in range(n):
      print(i, j)
  # O(n)    
  for k in range(n):
    print(k)
      
      
# O(1) --> Constant time complexity: As n increases, the number of operations remains constant, runtime remains constant 
# Most Efficient big O
def add_items(n):
  return n + n

# print(add_items(1000))

# O(log n) --> Logarithmic Time Complexity
# def

# Different terms for input
# O(a) + O(b)
# O(a + b) --> simplest form, not O(n)
def print_items(a, b):
  for i in range(a):
    print(i)
  for j in range(b):
    print(j)
   
# O(a) * O(b)
# O(a * b) --> simplest form, not O(n^2)
def print_items(a, b):
  for i in range(a):
    for j in range(b):
      print(i,j)
      
# Big O of lists
my_list = [11, 3, 23, 7]
my_list.append(17) # O(1) {no reindexing}
my_list.pop() # O(1) {no reindexing}
my_list.pop(0) # O(n) {reindexing}
my_list.insert(2, 'hi') # O(n) {reindexing}
# searching for an item
# by value --> O(n)
# by index --> O(1)
item = my_list[3] # O(1) {}