def sum():
    a = 5
    b = 10
    print("The sum of a and b is :", a+b)
def product():
    a = 5
    b = 10
    print ("The product of a and b is :", a*b)
sum()
product()

def sum_with_parameters(x,y):
    print("The sum of", x,"and", y, "is:", x+y)
sum_with_parameters(3, 7)

def product_with_parameters(x,y):
    print("The product of", x, "and",y, "is:", x*y)
product_with_parameters(3,7)

def sum_with_return(x,y):
    return x+y
print("The sum of 4 and 6 is:", sum_with_return(4,6))

def product_with_return(x,y):
    return x*y
print ("The product of 4 and 6 is:", product_with_return(4,6))
  
m1 = int (input("Enter the ENG marks: "))
m2 = int (input("Enter the DZO marks:"))
m3 = int (input("Enter the MATH marks:"))
            
def sum_with_return(m1,m2,m3):
    return m1+m2+m3
total =  sum_with_return(m1,m2,m3)
print("The total marks:",total)

def average_with_return(total):
    return total/3
average = average_with_return(total)
print("The average marks is :", average)

if average >= 50 :
     print("Result:PASS")
else :
    print("Result: FAIL")