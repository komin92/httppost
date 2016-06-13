import sys
import requests


print ('1. pls your target url  : eg "http://www.example.com/User/user_search.php"\n2. pls your post data name  : eg  "userID"\n3. pls your post data start value : eg  40000   <--- it is int type\n4. pls number enter : eg  10 ... \n5. pls save file name :  "yourname.txt" \nEnjoy ' )
url = input("Pls url add : ")
key = input("Pls Key input : ")
value = input(" Pls value  add : ")
i = input("Pls raw Number add : ")
#name = input("pls save file name : ")
for x in range(i) :

  

  id =value+x

  r =  (requests.post(url , data = {key : id} ).text) 

  

  #sys.stdout = open (name,'a')

  

  print(r+'\n')

  

  