#DAY 2 OF LEARNING PYTHON 

# LISTS arecreated in the squared brackets "[]"
#lists are ordered and they allow the duplicate values also in the lists
x,y,z= ["vishnu","vardhan",20]
print(type(x))
print(type(z))
print(type(y))
print(x)
print(y)
print(z)

#list allows the duplicate values
x=["vishnu","vardhan","maxwell","messi","niniii","rose","vishnu"]
print(x)

# we can also get the length of the list 
x=["vishnu","vardhan","maxwell","messi","niniii","rose"]
print(x)
print(len(x))

# list item data types
x= ["vishnu","vardhan","ninii","maxi"]
y= [3,4,5,6,7,9]
z=[3.0,1.0,3.7]
print(x)
print(y)
print(z)
print(type(x),type(y),type(z))

#acess list items here like it is taking the index value
#indexing the list

x=["vishnu","vardhan","maxi","ninii"]
print(x)
print(x[2])

#negative indexing 
x=["vishnu","vardhan","maxi","ninii"]
print(x)
print(x[-3])

#range of the index
x=["vishnu","vardhan","maxi","ninii"]
print(x)
print(x[:4])

#Adding the list items we use the Append()
x=["vishnu","vardhan","maxi","ninii"]
x.append("python")
print(x)

#insert a new item in the list 
x=["vishnu","vardhan","maxi","ninii"]
x.insert(1,"python")
print(x)

#extend the list like adding the 2 list together 
x=["vishnu","vardhan","maxi","ninii"]
y=["vishnu","vardhan","maxwell","messi","niniii","rose"]
x.extend(y)
print(x)

#remove the list items 

x=["vishnu","vardhan","maxi","ninii"]
x.remove("vardhan")
print(x)

# sorting the list it will sort into alphabetic
x=["vishnu","vardhan","maxi","ninii"]
x.sort()
print(x)

#sort the numbers 
x=[10,23,43,134,1,34,0,100]
x.sort()
print(x)

# it will sort from the reverse  
x=[10,23,43,134,1,34,0,100]
x.sort(reverse=True)
print(x)

# reverse  it will arrenge from the right to the left
x=[10,23,43,134,1,34,0,100]
x.reverse()
print(x)

# joining the 2 list together 
x=["vishnu","vardhan","maxi","ninii"]
y=["vishnu","vardhan","maxwell","messi","niniii","rose"]
z=x+y
print(z)

