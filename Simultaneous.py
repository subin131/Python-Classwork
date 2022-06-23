#take input from the user
a=int(input("Enter a first number: "));
b=int(input("Enter a second number: "));
c=int(input("Enter a third number: "));
d=int(input("Enter a fourth number: "));
e=int(input("Enter a fifth number: "));
f=int(input("Enter a sixth number: "));


def simultaneous(a,b,c,d,e,f):
    distance=(a*e)-(b*d)
    dist_x=(c*e)-(b*f)
    dist_y=(a*f)-(c*d)
    x=(dist_x/distance)
    y=(dist_y/distance)
    print (x,y)

simultaneous(a,b,c,d,e,f)
