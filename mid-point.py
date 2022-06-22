#take two inputs from user
x1=int(input("Enter first number: "))
x2=int(input("Enter second number: "))
y1=int(input("Enter third number: "))
y2=int(input("Enter fourth number: "))

#function
def midPoint(x1,x2,y1,y2):
    mean=(x1+x2)/2+(y1+y2)/2
    
    print(f"The mid point of {x1}, {x2},{y1}, and {y2 } is {mean}")

midPoint(x1,x2,y1,y2)
    