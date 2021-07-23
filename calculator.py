


num = int(input("Number: "))
f_or_m = input("Feet or Meters: ")
f_or_m.lower()
def calculator():
    if f_or_m == "feet":
        number_of_meters = num  * 0.3048
        print(number_of_meters)
    if f_or_m == "meters":
        number_of_feet = num * 3.2808399
        print(number_of_feet)
calculator()
   


