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
    
 

print("****************MENU******************")
print("1.Sort By Cost L2H")
print("2.Sort By Cost H2L")
print("3.Sort By Rating L2H")
print("3.Sort By Rating H2L")
print("5.Sort By Discount L2H")
print("6.Sort By Discount H2L")
print("0.EXIT")
num = int(input("Enter your Option"))

lis=[["cost", True], ["cost", False], ["rating", True],["discunr",True],["discunr",False]]
data.sort(key = lambda el:el[lis[num-1][0]], reverse = lis[num-1][1])
print(data)




    
    
    
 
	