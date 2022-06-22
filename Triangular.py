#taking one integer from user
nums=int(input("Enter the number: "))

def TriangularNumber(nums):
    n=1;
    while n<nums:
        tri=n*(n+1)/2
        if tri<nums:
            print(tri)
        n+=1
    
TriangularNumber(nums)