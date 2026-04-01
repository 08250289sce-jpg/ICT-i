age = int(input("Enter your age: "))
if age >= 18: 
    registered_voter = input("Are you a registered voter? (true/False): ")
    registered_voter = registered_voter.lower()
    if registered_voter == "true":
        print("You are eligble to vote.")
    else: 
        print("You need to register to vote.")
else:
    print("You are not eligible to vote.")
