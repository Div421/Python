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
	
	
def myfilter(num):
        m=["Exit","brand","name","category"]
        temp="Enter a{0} name"
        inp =input((temp.format(m[num])))
        newobj = filter(lambda el: el[m[num]]==inp,data)
        for i in newobj:
            print(i)

print("1. Filter By Brand")
print("2. Filter By Name")
print("3. Filter By Category")
print("0. For EXIT")
num = int(input("Enter your Option"))
myfilter(num)