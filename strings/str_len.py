def str_len(name):
    c=0
    for char in name:
        c +=1
    return c
        
name=str(input("Enter a string: "))
print("Length of string {} = {}".format(name,str_len(name)))
