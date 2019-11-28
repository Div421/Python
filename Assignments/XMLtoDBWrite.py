#!/usr/bin/python
import xml.dom.minidom

# Open XML document using minidom parser
root = xml.dom.minidom.parse("users.xml")
users = root.documentElement
if users.hasAttribute("org"):
    print("Root element : %s" % users.getAttribute("org"))

mLis = []
for user in users.getElementsByTagName('user'):
    lis = []
    fname = user.getElementsByTagName('fname')[0]
    lis.append(fname.childNodes[0].data)
    lname = user.getElementsByTagName('lname')[0]
    lis.append(lname.childNodes[0].data)
    lis = tuple(lis)
    mLis.append(lis)
print(mLis)
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor(pymysql.cursors.DictCursor)


data = cursor.executemany("""INSERT INTO User (FNAME, LNAME) VALUES (%s,%s)""", mLis)


db.commit()
db.close()
