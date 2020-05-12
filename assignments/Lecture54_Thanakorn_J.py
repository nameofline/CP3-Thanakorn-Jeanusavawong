def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        return login()
def showMenu():
    print("Done !")
    print("-------K Shop-------")
    print("1. Calculator")
    print("2. Do nothing")
    MenuSelect()
def MenuSelect():
    userSelected = int(input(">>"))
    if userSelected==1:
        print(priceCalculate())
    elif userSelected==2:
        print("OK BYE")
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()