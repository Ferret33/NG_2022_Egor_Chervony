print("Quadratic equation: ax^2+bc+c=0")
a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))

discriminant= b**2-4*a*c
if discriminant<0:
    print("The equation has no solutions!")
elif discriminant ==0:
    print("The equation has only one solution: x="+ str(-b/(2*a)))
elif discriminant>0:
    print("The equation has two solutions: x1="+str((-b+discriminant**0.5)/(2*a)) +" x2="+ str((-b-discriminant**0.5)/(2*a)))