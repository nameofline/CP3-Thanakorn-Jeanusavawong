menuList = []
def showBill():
    print("Myfood".center(10,"-"))
    total = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total += menuList[i][1]
    print(total)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()