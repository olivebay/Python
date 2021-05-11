'''Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.'''

xset = {"a", "b"}
print(xset)

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

#I mean we can get any one as output (without the quotes) :

"""
{'a', 'b'}
{'b', 'a'}
"""

#sets can also contain numbers or other data types

yset = {1,2}
#or
zset = {True,False}

#lets now see something interesting

aset = {1,1}
print(aset)

#can u predict the output ?

#did u say {1,1}

#sorry but tht is not how sets work the output will be : {1}

#we will disscuss all these later on
