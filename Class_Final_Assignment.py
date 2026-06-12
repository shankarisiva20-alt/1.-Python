class FinalAssignment():
    def SubFields():
        print("""Sub-Fields in AI are:
        Machine Learning
        Neutral Netowrks
        Vision
        Robotics
        Speech Processing
        Natural Language processing""")    
    def OddEven():
        number=int(input("Enter the number"))
        if ((number%2)==0):
            print(number, "is Even number")
        else:
            print(number, "is Odd number")
    def MarriageEligibility():
        gender=input("Your Gender:")
        age=int(input("Your ager:"))
        if gender == "male":
            if age >= 21:
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")
        
        elif gender == "female":
            if age >= 18:
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")    
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area Formula : (height*breadth)/2")
        print("Area of Traingle: ", area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        perimeter=height1+height2+breadth1
        print("Perimeter formula : height1+height2+breadth")
        print("perimeter of triangle : ", perimeter)
 