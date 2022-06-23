#this is the equations of SUVAT
#enter the input from user
v=input("Enter the final velocity: ")
u=input("Enter the initial velocity: ")
s=input("Enetr the dsiplacement: ")
t=input("Enter the time: ")
a=input("Enter the accleration: ")



if s == "" and a == "":
    result = float(0.5 * (float(u) + float(v)) * float(t))
    print("The output is", result)

if v == "":
    result = float(u) + float(a) * float(t)
    print("The output is", result)

     