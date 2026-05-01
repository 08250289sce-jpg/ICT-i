name = input("Enter the name:")
greet = lambda x : print("Hello",x)
greet(name)

number = input("enter the number:")
talk = lambda x: print ("i like ",x)
talk(number)

even_odd  = lambda x: "Even" if x%2 == 0 else"Odd"
num = int(input("Enter a number:"))
print(even_odd(num))

arith = lambda x,y: (x+y, x-y, x*y, x/y)#return multi resunlt
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(arith(num1, num2)) 

mylist = [1,2,3,4,5,6,7,8]#using filter
even = filter(lambda x: x%2==0, mylist)
print(list(even))

mylist = [123456]
double = map (lambda x: x*2, mylist)
print(list(double))

mynewlist = (list(double))
double = map(lambda x: x/2, mynewlist)
print(list(mylist))

from functools import reduce
mylist = [1,2,3,4]
mul = reduce(lambda x, y: x*y, mylist)
print(mul)

positive_negative_zero = lambda x : "positive" if x>0 else "negative or zero" 
num = int(input("Enter the number:"))
print (positive_negative_zero(num))