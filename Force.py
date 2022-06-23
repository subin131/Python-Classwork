#calculate the force
# mass=int(input("Enter the mass: "))
# acc=int(input("Enter the value: "))

def calculateForce(mass,acc):
    if(mass==None):
        
        print("The accleration of the body is null so can't calculate force.")
    elif acc==None:
        
        print("The mass of the body is null so can't calculate force.")
        
    else:
        force=mass*acc
        print(f"The calculation of force is {force}")

calculateForce(100,10)
calculateForce(None,10)
calculateForce(100,None)
