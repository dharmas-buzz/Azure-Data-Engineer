# Datatypes

# creating and defining a list
fruits = ["mango", "apple", "dragonFruit"]

# add new item to the list
fruits.append("orange")

# modify the item in the list like dragonFruit --> Dragon Fruit
fruits[2] = "Dragon Fruit"

fruits2 = ["Banana", "Guava"]

# to merge 2 lists in a single list
fruits.extend(fruits2) # --> fruits = ["mango", "apple", "Dragon Fruit", "Banana", "Guava"]

# what if I do append to merge 2 lists
fruits.append(fruits2) # --> fruits = ["mango", "apple", "Dragon Fruit", ["Banana", "Guava"]]

# to delete last item from the list
fruits.pop()

# to delete specific item from the list
fruits.remove("apple") # --> this removes apple from the list

fruits.index("Dragon Fruit") # --> shows the position of the item in the list --> output = 2

len(fruits) # --> gives you the count of no of items in the list




# -----------------------------------------------------------------------------------------------------------------------------

my_tuple = ("mango", "apple", "banana")

cnt = my_tuple.count("mango")
print(cnt)

my_tuple = ("mango", "apple", "banana", "mango", "mango")
cnt = my_tuple.count("mango")
print(cnt) # --> to know count of particular item in the list

print(my_tuple.index("banana")) # --> to know the index of particular item in the list

print(my_tuple + ("orange", "guava"))
print(my_tuple)

# -----------------------------------------------------------

# work around to modify a tuple

my_tuple_temp = list(my_tuple) # --> first we neeed to convert tuple into list...by using temp variable and make it temp tuple
print(my_tuple)

my_tuple_temp[4] = "watermelon" # --> here we added a new item into the list
print(my_tuple_temp)

my_tuple = tuple(my_tuple_temp) # --> here we convert the list into tuple...by using tuple function
print(my_tuple)  

# -------------------------------------------------------------------------------------------------------

# SET: Set is a unordered datatype (which means the order is not guaranteed) and also it won't support indexing.
#       And additionally, set won't carry any duplicate values.

my_set={1, 2, 3, 4, 5, 5, 6, 7, 7, 8}
print(my_set) 
# Result = {1, 2, 3, 4, 5, 6, 7, 8} --> No duplicate values

my_set = {"mango", "banana", 1, 2, 3, 4, 5, 6, 7, 8}
print(my_set) 
# Result = {1, 2, 3, 4, 5, 6, 7, 8, 'mango', 'banana'} --> Unordered(No guaratee of order)

# to add new item to the set
my_set.add(9)

# ----------------------------------------------------------------------------------------------------

# DICTIONARY:

stu_info = {
    "name" : "Dharma",
    "age" : 26,
    "subjects" : ["Telugu", "English", "Kannada"]
}

print(stu_info)

# Result = {'name': 'Dharma', 'age': 26, 'subjects': ['Telugu', 'English', 'Kannada']}

print(type(stu_info))

# Result = <class 'dict'>

# --> To print specific item from dictionary
print(stu_info["name"]) # --> we have to use key & value pairs
# Result = Dharma

# --> To print specific item in the list
print(stu_info["subjects"][2]) # --> we hacve th specify tyhe index number
# Result = Kannada
#Another way
print(stu_info.get("age")) #--> we can use 'get' function

  # To add new item to the dictionary
stu_info["city"] = "Bangalore"
print(stu_info)
# Result = {'name': 'Dharma', 'age': 26, 'subjects': ['Telugu', 'English', 'Kannada'], 'city': 'Bangalore'} 

 # To modify something in the dictionary
stu_info["age"] = 25
print(stu_info) # --> just change whatever you want to change... Resault = {'name': 'Dharma', 'age': 25, 'subjects': ['Telugu', 'English', 'Kannada'], 'city': 'Bangalore'}
 
# This is new changes
