name = input ("Enter yourb name:")
days_borrowed = int(input("Enter number of  days the books was borrow:"))
days_late = int(input("Enter number of days late:"))
if (days_late ==0):
    print("no need for fine")
elif (days_late >= 1 and days_late <= 5):
    print ("nu. 5 per_day")
elif (days_late >= 6 and days_late <= 9):
    print ("nu.10 per_day")
else:
    print("nu.20 per day")
if(days_borrowed > 30):
    print ("warning! libary privilege may be restricted")
else:
    print("")