# by while loop
num = input("enter a number")
i=0
while i<11:
     multiple = num*i
     print(multiple)
     i+=1

# by for loop
num = input("enter a number:")
for i in range (1,11):
    mul = num * i
    print("{} x {} = {}".format(num,i,mul))
