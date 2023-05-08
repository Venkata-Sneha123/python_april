def fun(name,msg):
    print("Hello:",name,msg)

fun(name="mohan",msg="Good Morning")
fun(msg="Good Morning",name="mohan")

fun("mohan","Good morning")
fun("Good morning","mohan")

'''
o/p:
Hello: mohan Good Morning
Hello: mohan Good Morning
Hello: mohan Good morning
Hello: Good morning mohan
'''
