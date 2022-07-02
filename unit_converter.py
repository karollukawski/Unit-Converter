choice = -1

def get_lenght():
    
    lenght = int(input("Give the number of your lenght: "))
    
    print ()
    print ("1. Kilometers")
    print ("2. Meters")
    print ("3. Decymeters")
    print ("4. Centimeters")
    print ("5. Milimeters")
    print ("6. Yards")
    print ("7. Feet")
    print ("8. Inches")
    print ("9. Miles")
    print ("10. Sea miles")
    print ()

    lenght_unit = int(input("Give the number of your unit: "))

    if lenght_unit == 1:
        print ()
        print (str(lenght) + " km")
        print (str(lenght/1000) + " m")
        print (str(lenght/10000) + " dm")
        print (str(lenght/100000) + " cm")
        print (str(lenght/1000000) + " mm")
        print (str(round(lenght*0.000914400000282, 4)) + " yd")
        print (str(lenght*32808399) + " ft")
        print (str(lenght*393700787) + " in")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()

while True:
    print ()
    print ("0. Lenght")
    print ("1. Weight")
    print ("2. Time")
    print ("3. Area")
    print ("4. Volume")
    print ("5. Temperature")
    print ("6. Exit")
    print ()

    choice = int(input("Choose your option: "))

    if choice == 0:
        get_lenght()
    if choice == 1:
        print ()
    if choice == 2:
        print ()
    if choice == 3:
        print ()
    if choice == 4:
        print ()
    if choice == 5:
        print ()
    if choice == 6:
        break    