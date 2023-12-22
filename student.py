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
t3=f.getvalue("t3")
t4=f.getvalue("t4")
t5=f.getvalue("t5")
t6=f.getvalue("t6")
t7=f.getvalue("t7")
t8=f.getvalue("t8")
t9=f.getvalue("t9")

btn=f.getvalue("b1")
try:
 if(btn=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['student']
#Primary key:
  k=0
  for x in collection.find({}):
        if(x["t1"]==t1):
                k=1
                break
  if(k==1):
      print("<script>alert('Error id .....')</script>")
  else:
   insert1={'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9}
   collection.insert_one(insert1)
   print("<script>alert('Welldone..Saved On student_save form.....')</script>")
   print("<script>window.open('Student_save.html','_self')</script>")
   
   
#Update Button:
 if(btn=="Update"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['student']
  collection.update_one({'t1':t1},{'$set':{'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9}})
  print("<script>alert('Record Update .....')</script>")
  print("<script>window.open('Student_update.html','_self')</script>")
  
#Delete Button:
 if(btn=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['student']
  s={'t1':t1}
  collection.delete_many(s)
  print("<script>alert('Record Deleted.....')</script>")
  print("<script>window.open('Student_save.html','_self')</script>")

#All Search Buttton:
 if(f.getvalue("b1")=="Allsearch"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['student']
  print("<center><table border=15 cellpadding=5 bgcolor=skyblue><tr><th>Student Id</th><th>Student Fname</th><th>Student Lname</th><th>Student Ccourse</th><th>Student Course</th> <th> Student Year</th> <th> student Contact  </th> <th>Student Age</th> <th> student age</th> <th> Student Gender</th></tr>")
  for x in collection.find({}):
      print("<tr><th>",x["t1"],"</th>","<th>",x["t2"],"</th>","<th>",x["t3"],"</th>","<th>",x["t4"],"</th>","<th>",x["t5"],"</th>","<th>",x["t6"],"</th>","<th>",x["t7"],"</th>"
          ,"<th>",x["t8"],"</th>","<th>",x["t9"],"</th>""< /tr>")  
#Paticular Search:
 if(f.getvalue("b1")=="Psearch"): 
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['student']
  print("<center><table border=15 cellpadding=5 bgcolor=skyblue><tr><th>Student Id</th><th>Student Fname</th><th>Student Lname</th><th>Student Ccourse</th><th>Student Course</th> <th> Student Year</th> <th> student Contact  </th> <th>Student Age</th> <th> student age</th> <th> Student Gender</th></tr>")
  for x in collection.find({'t1':t1}):
    print("<tr><th>",x["t1"],"</th>","<th>",x["t2"],"</th>","<th>",x["t3"],"</th>","<th>",x["t4"],"</th>","<th>",x["t5"],"</th>","<th>",x["t6"],"</th>","<th>",x["t7"],"</th>"
          ,"<th>",x["t8"],"</th>","<th>",x["t9"],"</th>""</tr>")  
except Exception:
    traceback.print_exc()
