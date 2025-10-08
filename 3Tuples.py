# DAY 2 OF LEARNING OF PYTHON 

#Tuples are used to store multiple items in a single variable. ex - x=("vishnu",12,3.0) single variable and multiple values 

#TUPLES these are indicted in the brackects "( )"
#these is how we print the tuples values 
x=("vishnu",12,3.0)
print(x)

#tuples always start from the index of 0 only 

#tuples can allow the multiple values 
x=("vishnu",12,3.0,12)
print(x)

# tuple length 
print(len(x))
print(type(x))

a= ("vishnu")
print(a)
print(type(a))
print(len(a))

#python data types
x = ("apple", "banana", "cherry")
y = (1, 5, 7, 9, 3)
z = (True, False, False) 

print(x,y,z)

#access the tuples here what we are indexing it show that item in the tuple only here also

x = ("apple", "banana", "cherry")
print(x[-1])


#range of tuple it starts from which number we are giving and till the last number it will come 
x = ("apple", "banana", "cherry")
print(x[0:3])

# negative range numbers also we can give it there 
x = ("apple", "banana", "cherry")
print(x[-3:-1])

#append the tuple 
x = ("apple", "banana", "cherry")
x.append("vishnu")
print(x)

