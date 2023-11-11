num1 = 11 # pointing var num1 at integer 11
num2 = num1 

print("Before num2 is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22
print("\nAfter num2 is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# Integers are immutable, that's why when we updated the value of num2, it doesn't overwrite the initial memory space of num2, instead, it assigns another memory space for the updated num2.

dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# Dictionaries are mutable, the value can be changed by a pointer

dict3 = {'value': 33}
dict2 = dict3
dict1 = dict2

# Garbage collection then occurs at dict1's initial value, because it has no variableprint("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 
print("dict3 =", dict3) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict3 points to:", id(dict3))

