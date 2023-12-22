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
t10=f.getvalue("t10")
t11=f.getvalue("t11")
btn=f.getvalue("b1")
try:
 if(btn=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Book_return_rec']
  
  #Primary key:
  k=0
  for x in collection.find({}):
        if(x["borrowerid"]==t1):
                k=1
                break
  if(k==1):
      print("<script>alert('Error id .....')</script>")
  else:
   insert1={'borrowerid':t1,'bookid':t2,'btitle':t3,'sid':t4,'sfnm':t5,'staffid':t6,'staffnm':t7,'stud_no_copy':t8,'reldate':t9,'duedate':t10,'bookdtret':t11}
   collection.insert_one(insert1)
   print("<script>alert('Record Saved.....')</script>")
   print("<script>window.open('Book_return_record_save.html','_self')</script>")
   
  #Updte button 
 if(f.getvalue("b1")=="Update"):   
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Book_return_rec']
  collection.update_one({'borrowerid':t1},{'$set':{'bookid':t2,'btitle':t3,'sid':t4,'sfnm':t5,'staffid':t6,'staffnm':t7,'stud_no_copy':t8,'reldate':t9,'duedate':t10,'bookdtret':t11}})
  print("<script>alert('Record Update sir  .....')</script>")
  print("<script>window.open('Book_return_record_update.html','_self')</script>")
  #Delete Button:
 if(btn=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Book_return_rec']
  s={'borrowerid':t1}
  collection.delete_many(s)
  print("<script>alert('Record Deleted.....')</script>")
  print("<script>window.open('Book_return_record_save.html','_self')</script>")
#All Search Buttton:
 if(f.getvalue("b1")=="Allsearch"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Book_return_rec']
  print("<center><table border=15 cellpadding=5 bgcolor=skyblue><tr><th>Borrowers ID</th><th>Book ID</th><th>Book Tittle</th><th>Student First Name</th><th>Staff ID</th><th>Staff First Name</th><th>Student NO Copies</th><th>Release Date</th><th>Due Date</th><th>Book day</th></tr>")
  for x in collection.find({}):
     print("<tr><th>",x["borrowerid"],"</th>","<th>",x["bookid"],"</th>","<th>",x["btitle"],"</th>","<th>",x["sid"],"</th>","<th>",x["sfnm"],"</th>","<th>",x["staffid"],"</th>","<th>",x["staffnm"],"</th>"
          ,"<th>",x["stud_no_copy"],"</th>","<th>",x["reldate"],"</th>","<th>",x["duedate"],"</th>","<th>",x["bookdtret"],"</th>""</tr>")

#Paticular Search: 
 if(f.getvalue("b1")=="Psearch"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['library']
  collection=db['Book_ret_rec']
  print("<center><table border=15 cellpadding=5 bgcolor=skyblue><tr><th>Borrower Id</th><th>Book Id</th><th>Book Title</th><th>stuid</th><th>sfnm</th><th>staff_id</th><th>staff_nm</th><th>student_no_copy</th><th>relase_date</th><th>due_date</th><th>book_date_return</th></tr>")
  for x in collection.find({'borrowerid':t1}):
    print("<tr><th>",x["borrowerid"],"</th>","<th>",x["bookid"],"</th>","<th>",x["btitle"],"</th>","<th>",x["sid"],"</th>","<th>",x["sfnm"],"</th>","<th>",x["staffid"],"</th>","<th>",x["staffnm"],"</th>"
          ,"<th>",x["stud_no_copy"],"</th>","<th>",x["reldate"],"</th>","<th>",x["duedate"],"</th>","<th>",x["bookdtret"],"</th>""</tr>")    
     
except Exception:
    traceback.print_exc()
