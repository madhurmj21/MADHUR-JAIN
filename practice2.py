
mylist= [1,2,3,5,4,6,9]
'''
a= sum(mylist)
print(a)
'''
# doing it by function
#def is_sum(mylist):
 #   return sum(mylist)

def is_sum (mylist):
    sum = 0
    for items in mylist():
       sum+=items
    return sum
        