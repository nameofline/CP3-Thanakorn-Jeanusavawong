systemMenu = {'หมูทอด':30,'กระเพรา':40,'ไข่เจียว':10,'ไข่ดาว':7,'ข้าวเปล่า':5}
menuList = []
def showBill():
    print("Myfood".center(10,"-"))
    total = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total += menuList[i][1]
    print("total :",total)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()