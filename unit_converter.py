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
    print ("11. Back to previous section")
    print ()

    lenght_unit = int(input("Give the number of your unit: "))

    if lenght_unit == 1:
        print ()
        print ("Basic unit: " + str(lenght) + " km")
        print ()
        print ("Conversions:")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(round(lenght*1093.61329833771, 4)) + " yd")
        print (str(lenght*3280.8399) + " ft")
        print (str(lenght*39370.0787) + " in")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()
    if lenght_unit == 2:
        print ()
        print ("Basic unit: " + str(lenght) + " m")
        print ()
        print ("Conversions:")
        print (str(lenght/1000) + " km")
        print (str(lenght*10) + " dm")
        print (str(lenght*100) + " cm")
        print (str(lenght*1000) + " mm")
        print (str(round(lenght*1.09361329833771, 4)) + " yd")
        print (str(round(lenght*3.2808399, 4)) + " ft")
        print (str(round(lenght*39.3700787, 4)) + " in")
        print (str(round(lenght*0.000621371192, 4)) + " mi")
        print (str(round(lenght*0.0005399568, 4)) + " nmi")
        print ()
    if lenght_unit == 3:
        print ()
        print ("Basic unit: " + str(lenght) + " dm")
        print ()
        print ("Conversions:")
        print (str(lenght/10000) + " km")
        print (str(lenght/10) + " m")
        print (str(lenght*10) + " cm")
        print (str(lenght*100) + " mm")
        print (str(round(lenght*0.109361329833771, 4)) + " yd")
        print (str(round(lenght*0.32808399, 4)) + " ft")
        print (str(round(lenght*3.93700787, 4)) + " in")
        print (str(round(lenght*0.0000621371192, 5)) + " mi")
        print (str(round(lenght*0.00005399568)) + " nmi")
        print ()
    if lenght_unit == 4:
        print ()
        print ("Basic unit: " + str(lenght) + " cm")
        print ()
        print ("Conversions:")
        print (str(lenght/100000) + " km")
        print (str(lenght/100) + " m")
        print (str(lenght/10) + " dm")
        print (str(lenght*10) + " mm")
        print (str(round(lenght*0.0109361329833771, 4)) + " yd")
        print (str(round(lenght*0.032808399, 4)) + " ft")
        print (str(round(lenght*0.393700787, 4)) + " in")
        print (str(round(lenght*0.00000621371192, 8)) + " mi")
        print (str(round(lenght*0.000005399568, 8)) + " nmi")
        print ()
    if lenght_unit == 5:
        print ()
        print ("Basic unit: " + str(lenght) + " mm")
        print ()
        print ("Conversions:")
        print (str(lenght/1000000) + " km")
        print (str(lenght/1000) + " m")
        print (str(lenght/100) + " dm")
        print (str(lenght/10) + " cm")
        print (str(round(lenght*0.00109361329833771, 4)) + " yd")
        print (str(round(lenght*0.0032808399, 4)) + " ft")
        print (str(round(lenght*0.0393700787, 4)) + " in")
        print (str(round(lenght*0.000000621371192, 9)) + " mi")
        print (str(round(lenght*0.0000005399568, 9)) + " nmi")
        print ()
    if lenght_unit == 6:
        print ()
        print ("Basic unit: " + str(lenght) + " yd")
        print ()
        print ("Conversions:")
        print (str(lenght) + " km")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(lenght*3280.8399) + " ft")
        print (str(lenght*39370.0787) + " in")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()
    if lenght_unit == 7:
        print ()
        print ("Basic unit: " + str(lenght) + " ft")
        print ()
        print ("Conversions:")
        print (str(lenght) + " km")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(round(lenght*1093.61329833771, 4)) + " yd")
        print (str(lenght*39370.0787) + " in")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()
    if lenght_unit == 8:
        print ()
        print ("Basic unit: " + str(lenght) + " in")
        print ()
        print ("Conversions:")
        print (str(lenght) + " km")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(round(lenght*1093.61329833771, 4)) + " yd")
        print (str(lenght*3280.8399) + " ft")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()
    if lenght_unit == 9:
        print ()
        print ("Basic unit: " + str(lenght) + " mi")
        print ()
        print ("Conversions:")
        print (str(lenght) + " km")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(round(lenght*1093.61329833771, 4)) + " yd")
        print (str(lenght*3280.8399) + " ft")
        print (str(lenght*39370.0787) + " in")
        print (str(round(lenght*0.5399568, 4)) + " nmi")
        print ()
    if lenght_unit == 10:
        print ()
        print ("Basic unit: " + str(lenght) + " nmi")
        print ()
        print ("Conversions:")
        print (str(lenght) + " km")
        print (str(lenght*1000) + " m")
        print (str(lenght*10000) + " dm")
        print (str(lenght*100000) + " cm")
        print (str(lenght*1000000) + " mm")
        print (str(round(lenght*1093.61329833771, 4)) + " yd")
        print (str(lenght*3280.8399) + " ft")
        print (str(lenght*39370.0787) + " in")
        print (str(round(lenght*0.621371192, 4)) + " mi")
        print ()
    if lenght_unit == 11:
        return

def get_weight():
    
    weight = int(input("Give the number of your lenght: "))
    
    print ()
    print ("1. Tons")
    print ("2. Kilograms")
    print ("3. Decagrams")
    print ("4. Grams")
    print ("5. Milimgram")
    print ("6. Pounds")
    print ("7. Back to previous section")
    print ()

    weight_unit = int(input("Give the number of your unit: "))

def get_time():
    
    time = int(input("Give the number of your lenght: "))
    
    print ()
    print ("1. Hours")
    print ("2. Minutes")
    print ("3. Seconds")
    print ("4. Miliseconds")
    print ("5. Back to previous section")
    print ()

    time_unit = int(input("Give the number of your unit: "))

def get_area():
    return
def get_volume():
    return
def get_temperature():
    
    temperature = int(input("Give the number of your lenght: "))
    
    print ()
    print ("1. Celsious")
    print ("2. Kelvins")
    print ("3. Fahrenheit")
    print ("4. Back to previous section")
    print ()

    temperature_unit = int(input("Give the number of your unit: "))
    
while True:

    print ()
    print ("1. Lenght")
    print ("2. Weight")
    print ("3. Time")
    print ("4. Area")
    print ("5. Volume")
    print ("6. Temperature")
    print ("7. Exit")
    print ()

    choice = int(input("Choose your option: "))

    if choice == 1:
        get_lenght()
    if choice == 2:
        get_weight()
    if choice == 3:
        get_time()
    if choice == 4:
        get_area()
    if choice == 5:
        get_volume()
    if choice == 6:
        get_temperature()
    if choice == 7:
        break    
