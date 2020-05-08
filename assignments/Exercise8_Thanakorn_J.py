usernameInput = input("Username ")
passwordInput = input("Password ")
if usernameInput == "admin" and passwordInput == "10011001":
    print("Done !")
    print("*************************************")
    print("---------Welcome to K Cocktails---------")
    print("   -List-           -Unit price(USD)-")
    print("1.  Mojito                 8.95")
    print("2.  Raspberry Cup          10.95")
    print("3.  Back's Vier            2.15")
    print("4.  Peroni                 4.5")
    print("5.  Magners                4.25")
    userSelected = int(input("Please choose your Cocktail >> "))
    if userSelected == 1:
        print("--------------You Choose Mojito--------------")
        unit = int(input("Unit : "))
        result = 8.95 * unit
        print("Total price(USD) :", result)
        print("-----------------K Cocktails-----------------")
        print("-----Thank you,Hope to see you next time-----")
    elif userSelected == 2:
        print("-----------You Choose Raspberry Cup----------")
        unit = int(input("Unit : "))
        result = 10.95 * unit
        print("Total price(USD) :", result)
        print("-----------------K Cocktails-----------------")
        print("-----Thank you,Hope to see you next time-----")
    elif userSelected == 3:
        print("-----------You Choose Back's Vier------------")
        unit = int(input("Unit : "))
        result = 2.15 * unit
        print("Total price(USD) :", result)
        print("-----------------K Cocktails-----------------")
        print("-----Thank you,Hope to see you next time-----")
    elif userSelected == 4:
        print("--------------You Choose Peroni--------------")
        unit = int(input("Unit : "))
        result = 4.5 * unit
        print("Total price(USD) :", result)
        print("-----------------K Cocktails-----------------")
        print("-----Thank you,Hope to see you next time-----")
    elif userSelected == 5:
        print("--------------You Choose Magners-------------")
        unit = int(input("Unit : "))
        result = 4.25 * unit
        print("Total price(USD) :", result)
        print("-----------------K Cocktails-----------------")
        print("-----Thank you,Hope to see you next time-----")
else:
    print("Username or password is incorrect !")
