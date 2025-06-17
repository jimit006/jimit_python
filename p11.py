# CRUD in python

# C :-  Create

# R :-  Read

# U :-  Update

# D :-  Delete

# CRUD, which stands for Create, Read, Update, and Delete, is a set of fundamental operations performed on data in databases and other data storage systems. It's a core concept in software development, web applications, and database management. Essentially, CRUD operations allow users to manage data by adding new entries, retrieving existing ones, modifying them, and removing them when no longer needed. 

# Examples

users = [
  {"id":1 , "name":"Alice" , "age":25},
  {"id":2 , "name":"Melisha" , "age":30}
 ]

while True:
  print("CRUD Operation in Python!!!!")
  print("1. create user")
  print("2. read user")
  print("3. update user")
  print("4. delete user")
  print("5. exit")

  choice = input("Enter your Choice(1-5) : ")

  if choice == "1":

    try:
      user_id = int(input("Enter id : "))
      name = input("Enter Name : ")
      age = int(input("Enter age : "))
      users.append({"id":user_id , "name":name , "age":age})

      print ("User Successfully Added!!")

    except:
      print("Invalid Input!!")

  elif choice == "2":
    if not users:
      print("No User found.")
    else:
      print("User List:")
      for user in users:
        print(user)

  # elif choice == "3":
  #   try:

  #     user_id = int(input("Enter Update user id : "))

  #     for user["id"]

  #   except:

    
# users = [
#   {"id":1 , "name":"Alice" , "age":25},
#   {"id":2 , "name":"Melisha" , "age":30}
#  ]

# for user["id"] == user_id in users:
#   print(user)