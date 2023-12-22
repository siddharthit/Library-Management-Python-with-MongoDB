#! C:/Users/91810/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi 
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
btn=f.getvalue("b1")
try:
 if(btn=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Admin']
  insert1={'Username':t1,'Password':t2}
  collection.insert_one(insert1)
  print("<script>alert(' Client Saved .....')</script>")
 if(btn=="Login"):
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['library']
    collection=db['Admin']
    k=0
    for x in collection.find({}):
        if(x["Username"]==t1):
            if(x["Password"]==t2):
                k=1
                break
    if(k==1):
        print("<script>window.open('menu.html','_self')</script>")
    else:
        print("<script>alert(' Login Failed .....')</script>")
  
except Exception:
    traceback.print_exc()

