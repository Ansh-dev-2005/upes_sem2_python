# Calculate area of shapes from user input using functions

def area_of_circle(r):
    return 3.14*r*r
def area_of_rectangle(l,b):
    return l*b
def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
def area_of_square(s):
    return s*s
def area_of_parallelogram(b,h):
    return b*h
def area_of_trapezium(a,b,h):
    return 0.5*(a+b)*h
def area_of_rombus(d1,d2):
    return 0.5*d1*d2
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")
print("4. Area of Square")
print("5. Area of Parallelogram")
print("6. Area of Trapezium")
print("7. Area of Rombus")
print("8. Area of Semi Circle")
print("9. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        r = float(input("Enter radius of circle: "))
        print("Area of circle is",area_of_circle(r))
    elif choice == 2:
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))
        print("Area of rectangle is",area_of_rectangle(l,b))
    # Apply herons formula for triangle and add contidiion weaher it is traingle or not
    elif choice == 3:
        a=float(input("Enter first side of triangle: "))
        b=float(input("Enter second side of triangle: "))
        c=float(input("Enter third side of triangle: "))
        if(a+b<=c or b+c<=a or a+c<=b):
            print("Triangle is not possible")
            continue
        print("Area of triangle is",area_of_triangle(a,b,c))
    elif choice == 4:
        s = float(input("Enter side of square: "))
        print("Area of square is",area_of_square(s))
    elif choice == 5:
        b = float(input("Enter base of parallelogram: "))
        h = float(input("Enter height of parallelogram: "))
        print("Area of parallelogram is",area_of_parallelogram(b,h))
    elif choice == 6:
        a = float(input("Enter first side of trapezium: "))
        b = float(input("Enter second side of trapezium: "))
        h = float(input("Enter height of trapezium: "))
        print("Area of trapezium is",area_of_trapezium(a,b,h))
    elif choice == 7:
        d1 = float(input("Enter first diagonal of rombus: "))
        d2 = float(input("Enter second diagonal of rombus: "))
        print("Area of rombus is",area_of_rombus(d1,d2))
    elif choice == 8:
        r=int(input("Enter radius of Semi circle: "))
        print("Area of Semi circle is",area_of_circle(r)/2)
    elif choice == 9:
        # ask user if there is group of shapes and calculate area of all shapes
        a=int(input("Enter number of shapes: "))
        for i in range(a):
            print("1. Area of Circle")
            print("2. Area of Rectangle")
            print("3. Area of Triangle")
            print("4. Area of Square")
            print("5. Area of Parallelogram")
            print("6. Area of Trapezium")
            print("7. Area of Rombus")
            print("8. Area of Semi Circle")
            print("9. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                r = float(input("Enter radius of circle: "))
                print("Area of circle is",area_of_circle(r))
            elif choice == 2:
                l = float(input("Enter length of rectangle: "))
                b = float(input("Enter breadth of rectangle: "))
                print("Area of rectangle is",area_of_rectangle(l,b))
            # Apply herons formula for triangle and add contidiion weaher it is traingle or not
            elif choice == 3:
                a=float(input("Enter first side of triangle: "))
                b=float(input("Enter second side of triangle: "))
                c=float(input("Enter third side of triangle: "))
                if(a+b<=c or b+c<=a or a+c<=b):
                    print("Triangle is not possible")
                    continue
                print("Area of triangle is",area_of_triangle(a,b,c))
            elif choice == 4:
                s = float(input("Enter side of square: "))
                print("Area of square is",area_of_square(s))
            elif choice == 5:
                b = float(input("Enter base of parallelogram: "))
                h = float(input("Enter height of parallelogram: "))
                print("Area of parallelogram is",area_of_parallelogram(b,h))
            elif choice == 6:
                a = float(input("Enter first side of trapezium: "))
                b = float(input("Enter second side of trapezium: "))
                h = float(input("Enter height of trapezium: "))
                print("Area of trapezium is",area_of_trapezium(a,b,h))
            elif choice == 7:
                d1 = float(input("Enter first diagonal of rombus: "))
                d2 = float(input("Enter second diagonal of rombus: "))
                print("Area of rombus is",area_of_rombus(d1,d
    elif choice == 10:
        break
    else:
        print("Invalid choice")
