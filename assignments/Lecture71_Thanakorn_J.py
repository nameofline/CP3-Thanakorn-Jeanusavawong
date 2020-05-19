def showBill():
    print("Myfood".center(10,"-"))
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        total = 0
        for price in priceList:
            total += price
    print("total :",total)
menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()