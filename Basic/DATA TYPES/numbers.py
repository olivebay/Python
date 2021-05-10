"""Numbers can be further divided into Integers, Floats, Complex and Booleans."""
"""I am not going to describe booleans here"""

#Lets try seeing Integers first

"""Example:1-"""
print(type(5))
#This will give us the output as : <class 'int'>

"""Example:2-"""
A = 1  #here A is an integers
#we can verify it using the type() function - 
B = type(A) #using the type function 
print B #printing the value of B
#The above will get output as : <class 'int'>


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Lets now try floats

"""Example:1-"""
print(type(5.5))
#This will give us the output as : <class 'float'>

"""Example:2-"""
C = 1.8  #here A is an integers
#we can verify it using the type() function - 
C = type(D) #using the type function 
print D #printing the value of B
#The above will get output as : <class 'float'>

"""Example:3-"""
print(type(-7.5))
#This will also give us the output as : <class 'float'>

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Lets try complex numbers shall we ;-)
#Note - Python treats the imaginary number i as j

"""Example:1-"""
print(type(5.5+1j))
#This will give us the output as : <class 'complex'>

"""Example:2-"""
print(type(5.5+j))
#However this will return us an error
"""Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'j' is not defined"""
#Because j need to have a coefficient inorder to be treated as a complex error 
#here j is being treated as a variable which has no value thus this error

"""Example:3-"""
#We can do a similar thing by assigning the value of a complex number to a variable
h = -5.5+2j
print(type(h))
#Output will be : <class 'complex'>

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

