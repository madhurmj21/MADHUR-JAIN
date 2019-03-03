d1 = {1:10, 2: 30}
d2 = {3:50, 4: 60}
d3 = {5:70, 6: 80}
d4 = {}
'''
# using direct method 
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)
'''
# using for loop
for dictionariesd in  (d1,d2,d3): 
       d4.update(dictionariesd)
print(d4)