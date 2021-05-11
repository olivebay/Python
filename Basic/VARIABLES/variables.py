#Python has no command for declaring a variable.

#A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)
#we will get output as : "Sally"

#If you want to specify the data type of a variable, this can be done with casting.

c = str(3)    # x will be '3'
d = int(3)    # y will be 3
e = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.

f = 5
g = "John"
print(type(x)) #It will be integer
print(type(y)) #It will be string

#String variables can be declared either by using single or double quotes:
h = "John"
# is the same as
g = 'John'
#Try checking it using print


k = 4
K = "Sally"
#K will not overwrite k
