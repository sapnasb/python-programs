#This program calculates simple interest

def interest(p, t, r):
    
    Simple_Interest =(p * t * r)/100

    Principle_Amount =(p)

    Total_Value =(Simple_Interest + p)

    print("The Simple Interest : ", Simple_Interest)
    print("Principle amount : ", Principle_Amount)
    print("Total Value : ", Total_Value)

    
    return Simple_Interest
    return Principle_Amount
    return Total_Value

p = int(input("Enter the Principle: "))
t = int(input("Enter the Time: "))
r = int(input("Enter the Rate of Interest: "))

interest(p, t, r)