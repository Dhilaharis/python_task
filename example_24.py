import math

#area of triangle
def triangle():
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    z=int(input("enter z:"))
    s=(x+y+z)/2
    area_triangle=math.sqrt(s*(s-x)*(s-y)*(s-z))
    print(f"AREA OF TRIANGLE IS:",{area_triangle})
triangle()

#area of square
def square():
    a=int(input("Enter a:"))
    area_square=a*a
    print("AREA OF SQUARE IS:",area_square)
square()

#area of rectangle
def rectangle():
    l=int(input("enter l:"))
    w=int(input("enter w:"))
    area_rectangle=l*w
    print(f"AREA OF RECTANGLE IS:",{area_rectangle})
rectangle()

#area of circle
def circle():
    r=int(input("enter r:"))
    area_circle=math.pi*r*r
    print(f"AREA OF CIRCLE IS:",{area_circle})
circle()

#area of trapezium
def trapezium():
    a=int(input("enter a:"))
    b=int(input("enter h:"))
    h=int(input("enter h:"))
    area_trapezium=((a+b)/2)*h
    print(f"AREA OF TRAPEZIUM IS:",{area_trapezium})
trapezium()


