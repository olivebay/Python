'''Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.'''



'''Important  Note - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.'''


t = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(t)

#will give : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

th = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(th["brand"])

#will give the output as : Ford

#lets now consider something 

d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(d)

#will give output as :
'''{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}'''

#so duplicate values are overwriten

#lets see another example ti make the thing more clear 

e = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020,
  "year": 1964
}
print(e)

#this will give output as : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
