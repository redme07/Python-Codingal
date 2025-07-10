medical_cause = input("Did you have a medical cause Y for yes and N for no : ")

attendence = float(input("Enter your attendance : "))

if(medical_cause == "Y"):
    print("Exam entry allowed")

else:
    if(attendence >= 75):
        print("Exam entry allowed")
    else:
        print("Not allowed")
