user=str(input("Do you have a medical cause Y for yes N for No:"))
attend=int(input("Enter your attendance:"))
if user=="Y":
    print("You are eligibal to sit for the exam")
if user=="N":
 if attend>75:
    print("You are eligibal to sit for the exam")
 else:
    print("You are not eligibal to sit for the test")