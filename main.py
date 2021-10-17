print("Hello user! If you want convert kilometers into miles, then enter number of kilometers")

a = "yes"

while a == "yes":
    km = float(input("Enter number of kilometers: "))
    miles = km * 0.621
    print(str(km) + " km = " + str(miles) + " miles")

    a = input("Do you want to repeat the calculation? yes/no: ")

    if a == "yes":
        continue
    else:
        print("Goodbye!")