myList=['a','a','a','a','a','b','b','b','b','b','b','z','z','d','d','e','c','c','c']
d={}
for list in myList:
    d[list]=d.get(list,0)+1
print(d)