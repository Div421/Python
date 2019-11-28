dict={
    "Sachin":"icc",
    "Saurav":"BCCI"
}

class NameNotFound(Exception):
    def __init__(self,msg="Name Not Found :("):
        Exception.__init__(self,msg)
class WrongPassword(Exception):
    def __init__(self,msg="Wrong Password :("):
        Exception.__init__(self,msg)


un='Sachin'
pw="icc"

'''for i in dict.keys():
    if i == un:
    input("Enter UserName")
    input("Enter Password")
        print(i)
        if dict[i] == pw:
            print(dict[i])
            print("Correct")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")'''

if un not in dict:
    raise NameNotFound

if pw is not dict[un]:
    raise WrongPassword

