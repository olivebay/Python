"""LETS TRY UNDERSTAND BOOLEANS WITH A FEW EXAMPLES"""

a = True 
print(type(a))

b = False
print(type(b))

#these will give the output as : <class 'bool'>
#make sure while defining booleans they are in the same form as mine (that is dont define it as TRUE or true or FALSE or false) or any other they should be (True or False)

"""LETS SEE SOME MORE EXAMPLES"""

c = True and False
print(type(c))
print(c)

'''The output will be :
<class 'bool'>
False''' #The value is using boolean algebra


d = True or False
print(type(d))
print(d)

'''The output will be :
<class 'bool'>
True''' #The value is using boolean algebra

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

e = 3>5 #an False condition will show the value as False
print(e)

f = 3<5 #an True condition will show the value as True
print(f)

h = "a" in "raw"
print(h) #the output will show value of h as True

g = "9" in "raw"
print(g) #the output will show value of g as False

#we are gonna learn more about these little later

#these can also be used in if...elif...else and loop statements
