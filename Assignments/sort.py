data=[{   "id":"001",
	"name":"phone",
	"cost":"10000",
	"brand":"realme",
	"rating":"5",
	"discounr":"10%",
	"category":"electronics"  },
{   "id":"002",
	"name":"watch",
	"cost":"5000",
	"brand":"fastrack",
	"rating":"4",
	"discounr":"5%",
	"category":"electronics"  },
{   "id":"003",
	"name":"bottle",
	"cost":"200",
	"brand":"tupperware",
	"rating":"1",
	"discounr":"10%",
	"category":"home"  },
{   "id":"004",
	"name":"Laptop",
	"cost":"60000",
	"brand":"hp",
	"rating":"5",
	"discounr":"10%",
	"category":"electronics"  },
{   "id":"005",
	"name":"phone",
	"cost":"15000",
	"brand":"iphone",
	"rating":"3",
	"discounr":"10%",
	"category":"electronics"  },
{   "id":"006",
	"name":"laptop",
	"cost":"100000",
	"brand":"hp",
	"rating":"5",
	"discounr":"50%",
	"category":"electronics"  },
{   "id":"007",
	"name":"watch",
	"cost":"12000",
	"brand":"sonata",
	"rating":"4",
	"discounr":"10%",
	"category":"electronics"  }	]
    
def mysort():
    def sortByCostL2H():
        mySort= lambda el:  int(el["cost"])
        data.sort(key=mySort)  
        print(data) 
    def sortByCostH2L():
        mySort= lambda el:  int(el["cost"])
        data.sort(key=mySort,reverse=True)  
        print(data) 
    def sortByRating():
        mySort= lambda el:  int(el["rating"])
        data.sort(key=mySort,reverse=True)  
        print(data)
    def sortByDiscountL2H():
        mySort= lambda el:  int(el["discunr"])
        data.sort(key=mySort)  
        print(data) 
    def sortByDiscountH2L():
        mySort= lambda el:  int(el["discunr"])
        data.sort(key=mySort,reverse=True)  
        print(data) 
    d={"1":sortByCostL2H,"2":sortByCostH2L,"3":sortByRating,"4":sortByDiscountL2H,"5":sortByDiscountH2L}
    return d
ss=mysort()
num=1
while num!=0
    print("****************MENU******************")
    print("1.Sort By Cost L2H")
    print("2.Sort By Cost H2L")
    print("3.Sort By Rating")
    print("4.Sort By Discount L2H")
    print("5.Sort By Discount H2L")
    print("0.EXIT")
    num = (input("Enter your Option"))
    ss[num]()
    
    
 
	