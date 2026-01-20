#WORKING WITH DICTIONARIES 
my_dict = {
   "key1": "value1",
   "key2": "value2",
   "key3": "value3"
}

ContactInformation = {
    "name": "Alex Teye",
    "age": 25,
    "phone_number": "0549044977",
    "email":" awonders001gmail.com"
}

print(ContactInformation["name"])
print(ContactInformation.get("email"))
print(ContactInformation.get("phone_number"))
print(ContactInformation.keys())
print(ContactInformation.values())
print(ContactInformation.get("age"))


My_Dic2 = {
    "name": "Joseph Atsu" ,
    "age": 30 ,
    "Residence": "Tesano" , 
    "Occupation" : " Medical Doctor",
    "email": "josephlabtech@gmail.com"

}


print(My_Dic2.get("name"))
print(My_Dic2.get("Occupation"))
print(My_Dic2.values())
print(My_Dic2.keys())
print(My_Dic2.get("Residence"))
print(My_Dic2.get("age"))

My_Dict3 ={
    "name": "Theophius Sunday",
    "age" : "26" ,
    "phone_number" : "0246505130",
    "email" : "awonders001@gmail.com",
    "Deparment": "Computer Science" ,
    "Address": "United Kingdom"
}


My_Dic2["phone_number" ] = +233549044977
My_Dic2["Residence"] = "Kumasi"
My_Dic2["Location"] = "United States of America"

del My_Dic2["email"]
print(My_Dic2)

for key,value in My_Dic2.items():
    print(f"{key}: {value}")

