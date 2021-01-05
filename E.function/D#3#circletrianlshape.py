def area_func():

    shape = input("Enter the shape to find the area : ")

    if shape == 'CIRCLE':
        r = float(input("Please enter the radius : "))
        area = 3.1416*pow(r, 2)
        print("The area of circle is : ", area)

    elif shape == 'TRIANGLE':
        base = float(input("Please enter the base : "))
        height = float(input("Please enter the height : "))
        area = 0.5*base*height
        print("The area of triangle is : ", area)

    elif shape == 'RECTANGLE':
        length = float(input("Please enter the length : "))
        width = float(input("Please enter the width : "))
        area = length * width
        print("The area of rectangle is : ", area)

    elif shape == 'TRAPEZIUM':
        a = float(input('Please enter the base1 : '))
        b = float(input('Please enter the base2 : '))
        height = float(input('Please enter the height : '))
        area = ((a+b)/2)*height
        print("The area of trapezium is : ", area)


area_func()
