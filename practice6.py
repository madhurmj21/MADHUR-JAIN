d1 = {1:5,2:5,3:50,5:80}
def is_key_present(x):
    if x in d1:
        print('{} key is present in the dictionary'.format(x))
    else:
        print('{} key is not present in the dictionary'.format(x))  
is_key_present(9)