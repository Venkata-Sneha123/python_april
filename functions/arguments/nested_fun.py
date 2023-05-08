def f1():
    print("hello")
    def f2():
        print("Hai")
        def f3():
            print("welcome")
        f3()
    f2()

f1()

'''
o/p:
hello
Hai
welcome
'''
