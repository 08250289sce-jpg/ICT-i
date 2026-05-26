Eng = int(input("Enter your eng marks:"))
Dzo = int(input("Enter your dzo marks:"))
Math = int(input("Enter your math marks:"))
Average = (Eng + Dzo + Math / 3)
print(Average)
if(Average>= 90 and Eng >= 50 and Dzo >= 50 and Math >= 50):
    print("Grade A")

elif(Average>= 80 and Eng >= 50 and Dzo >= 50 and Math >= 50):
    print("Grade B")

elif(Average>= 70 and Eng >= 50 and Dzo >= 50 and Math >= 50):
    print ("Grade C")

elif(Average>= 60 and Eng >= 50 and Dzo >= 50 and Math >= 50):
    print("Grade D")

elif(Average >= 50  and Eng >= 50 and Dzo >= 50 and Math >= 50):
    print("Grade E")

else:
    print("You are fail!...so hope you will do greate in next time")