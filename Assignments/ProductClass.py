class product:
    def __init__(o,i,n,c,b,r,d,ca):
        o.id=i
        o.name=n
        o.cost=c
        o.brand=b
        o.rating=r
        o.discount=d
        o.category=ca
    def showAll(self):

        print(self.name , self.cost,self.brand, self.rating,self.discount, self.category)
ob1 = product("001", "Phone",7000,"realme","5","20","Electronis")
ob2 = product("002","Laptop",70000,"hp","4","20","Electronis")
ob3 = product("003","Phone",12000,"realme","3","20","Electronis")
ob4 = product("004","Bottle",70,"tupperware","2","20","Home")
ob5 = product("005","Laptop",56000,"Dell","1","20","Electronis")
ob6 = product("006","Pendrive",1000,"hp","4","20","Electronis")
ob7 = product("007","Hard Disk",3000,"hp","2","20","Electronis")
ob8 = product("008","Bottle",200,"tupperware","3","20","Home")


print("****************MENU******************")
print("1.Sort By Cost L2H")
print("2.Sort By Cost H2L")
print("3.Sort By Rating L2H")
print("3.Sort By Rating H2L")
print("5.Sort By Discount L2H")
print("6.Sort By Discount H2L")
print("0.EXIT")
num = int(input("Enter your Option"))

objList=[ob1,ob2,ob3,ob4,ob5,ob6,ob7,ob8]
lis = [["cost", True], ["cost", False], ["rating", True], ["discount", True], ["discount", False]]

objList.sort(key=lambda el: el.cost)
for i in objList:
    i.showAll()



ob1.__getattribute__("name")
objList.sort(key=lambda el: el.getattr(el, lis[num-1][0]), reverse=lis[num-1][1])
for i in objList:
    i.showAll()






