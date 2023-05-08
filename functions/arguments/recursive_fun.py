def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print("Factorial of 4 is:",factorial(4))
print("Factorial of 5 is:",factorial(5))


'''
o/p:
Factorial of 4 is: 24
Factorial of 5 is: 120
'''
