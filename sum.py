#take two inputs from user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

#function
def sum(num1,num2):
    sum=num1+num2
    print(f"The sum of {num1} and {num2} is {sum}.")
    
sum(num1,num2)