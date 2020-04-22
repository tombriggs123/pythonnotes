#This is the documentation of my python learning, starting from basic knowledge.


#Dictonaries are like lists consisting of key value pairs.
myCat = {'size': 'fat','colour': 'grey', 'name': 'ted'}
print(myCat['size'])

#Dictonaries cannot be used with append() method, but they can be used in for loops
spam = {'color': 'red', 'age': 42}
for v in spam.values(): #Remember values not value
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

#When you use the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.

pinicITems = {'apples': 2, 'pears': 5}
print('I am bringing' + str(pinicITems.get('eggs', 0))) #Eggs doesn't exist in the dictionary, if you put apples, 0 it would return 2 instead of 0. Anything that doesn't exist
# it will print 0
