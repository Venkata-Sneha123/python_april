def f1(name,msg):
    print("Hello:",name,msg)
#keyword arguments
f1(name="mohan",msg="Good morning")
f1(msg="Good morning",name="mohan")
f1("mohan",msg="Good morning")
#f1(name="mohan","Good morning") #SyntaxError: positional argument follows keyword argument


'''
o/p:
Hello: mohan Good morning
Hello: mohan Good morning
Hello: mohan Good morning
'''
