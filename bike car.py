choice1=int(input("Which one do you like more car or bike for car say 1 and for bike say 2:"))
if choice1==1:  
    print("Select your car")
    print("1.Suv")
    print("2.Muv")
    print("3.Electric car")
    choice2=str(input("Enter your choice:"))
    if choice2==1:
        print("You have selected Suv")
    if choice2==2:
        print("You have selected Muv")
    if choice2==3:
        print("You have selected Electric car")
elif choice1==2:  
    print("Select your bike")
    print("1.Two wheeler")
    print("2.Scooter")
    print("3.Electric bike")
    choice2=str(input("Enter your choice:"))
    if choice2==1:
        print("You have selected Two wheeler")
    if choice2==2:
        print("You have selected Scooter")
    if choice2==3:
        print("You have selected Electric bike")
