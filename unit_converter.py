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

    if weight_unit == 1:
        print ()
        print ("Basic unit: " + str(weight) + " t")
        print ()
        print ("Conversions:")
        print (str(weight*1000) + " kg")
        print (str(weight*100000) + " dag")
        print (str(weight*1000000) + " g")
        print (str(weight*1000000000) + " mg")
        print (str(round(weight*2204.6226218, 4)) + " lbs")
        print ()
    if weight_unit == 2:
        print ()
        print ("Basic unit: " + str(weight) + " kg")
        print ()
        print ("Conversions:")
        print (str(weight/1000) + " t")
        print (str(weight*100) + " dag")
        print (str(weight*1000) + " g")
        print (str(weight*1000000) + " mg")
        print (str(round(weight*2.2046226218, 4)) + " lbs")
        print ()
    if weight_unit == 3:
        print ()
        print ("Basic unit: " + str(weight) + " dag")
        print ()
        print ("Conversions:")
        print (str(weight/100000) + " t")
        print (str(weight/100) + " kg")
        print (str(weight*10) + " g")
        print (str(weight*10000) + " mg")
        print (str(round(weight*0.022046226218, 4)) + " lbs")
        print ()
    if weight_unit == 4:
        print ()
        print ("Basic unit: " + str(weight) + " g")
        print ()
        print ("Conversions:")
        print (str(weight/1000000) + " t")
        print (str(weight/1000) + " kg")
        print (str(weight/10) + " dag")
        print (str(weight*1000) + " mg")
        print (str(round(weight*0.0022046226218, 4)) + " lbs")
        print ()
    if weight_unit == 5:
        print ()
        print ("Basic unit: " + str(weight) + " mg")
        print ()
        print ("Conversions:")
        print (str(weight/1000000000) + " t")
        print (str(weight/1000000) + " kg")
        print (str(weight/10000) + " dag")
        print (str(weight/1000) + " g")
        print (str(round(weight*0.0000022046226218, 6)) + " lbs")
        print ()
    if weight_unit == 6:
        print ()
        print ("Basic unit: " + str(weight) + " lbs")
        print ()
        print ("Conversions:")
        print (str(round(weight*0.0004535924, 4)) + " t")
        print (str(round(weight*0.4535924, 4)) + " kg")
        print (str(weight*45.35924) + " dag")
        print (str(weight*453.5924) + " g")
        print (str(weight*453592.4) + " mg")
        print ()
    if weight_unit == 7:
        return

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

    if time_unit == 1:
        print ()
        print ("Basic unit: " + str(time) + " h")
        print ()
        print ("Conversions:")
        print (str(time*60) + " min")
        print (str(time*3600) + " s")
        print (str(time*3600000) + " ms")
        print ()
    if time_unit == 2:
        print ()
        print ("Basic unit: " + str(time) + " min")
        print ()
        print ("Conversions:")
        print (str(round(time/60, 3)) + " h")
        print (str(time*60) + " s")
        print (str(time*60000) + " ms")
        print ()
    if time_unit == 3:
        print ()
        print ("Basic unit: " + str(time) + " s")
        print ()
        print ("Conversions:")
        print (str(round(time/3600, 4)) + " h")
        print (str(round(time/60, 3)) + " min")
        print (str(time*1000) + " ms")
        print ()
    if time_unit == 4:
        print ()
        print ("Basic unit: " + str(time) + " ms")
        print ()
        print ("Conversions:")
        print (str(round(time/3600000, 7)) + " h")
        print (str(round(time/60000, 6)) + " min")
        print (str(time/1000) + " s")
        print ()
    if time_unit == 5:
        return

def get_area():
    
    area = int(input("Give the number of your area: "))
    
    print ()
    print ("1. Square kilometers")
    print ("2. Square meters")
    print ("3. Square decymeters")
    print ("4. Square centimeters")
    print ("5. Square milimeters")
    print ("6. Hectares")
    print ("7. Ares")
    print ()

    area_unit = int(input("Give the number of your unit: "))

    if area_unit == 1:
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
    
    if temperature_unit == 1:
        print ()
        print ("Basic unit: " + str(temperature_unit) + " Celsious")
        print ()
        print ("Conversions:")
        print (str(temperature_unit + 274.15) + " Kelvins")
        print (str(temperature_unit + 33.8) + " Fahrenheit")
        print ()
    if temperature_unit == 2:
        print ()
        print ("Basic unit: " + str(temperature_unit) + " Kelvins")
        print ()
        print ("Conversions:")
        print (str(temperature_unit - 274.15) + " Celsious")
        print (str(temperature_unit - 457.85) + " Fahrenheit")
        print ()
    if temperature_unit == 3:
        print ()
        print ("Basic unit: " + str(temperature_unit) + " Fahrenheit")
        print ()
        print ("Conversions:")
        print (str(temperature_unit - 33.8) + " Celsious")
        print (str(temperature_unit + 457.85) + " Kelvins")
        print ()    
    if temperature_unit == 4:
        return
        
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
