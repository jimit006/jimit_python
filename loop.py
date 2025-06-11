# Break Statement in python

# for i in range(1 , 6):
#   if i == 4:
#     break
#   print("For Loop : " , i)

# continue Statement in python

# for i in range(1 , 6):
#   if i == 4:
#     continue
#   print("For Loop : " , i)

# Break and continue in Nested Loop +

# for i in range(1 , 4):
#   for j in range(1 , 2):
#     if j == 2:
#       break
#     print("j loop: ", j)
#   print("i loop: " , i)

# for i in range(1 , 4):
#     print("i loop: " , i)
#     for j in range(2):
#       if i == 2:
#         break 
#       print("j loop: " , j)

# Pattern Print in python

# for i in range(1 , 7):
#   for j in  range(1 , i):
#       print(f"{j}" , end="")
#   print()

# pattern print in python 

for i in range(1 , 7):
     for S in range(1 , i):  
         print(f"{S}" , end="")
     print()

# pattern 2

for i in range(6):
     for S in range(i , -1 , -1):  
         print(f"{S+1}" , end="")
     print()

# pattern 3

for i in range(1 , 7):
     for S in range(i):  
         print(f"{i}" , end="")
     print()

# pattern 4 

for i in range(5):
     for S in range(i+1):  
         print(f"{5-i}" , end="")
     print()


# pattern 5

for i in range(5):
     for S in range(i , -1 , -1):  
         print(f"{5-S}" , end="")
     print()


# pattern 6


for i in range(5):
    for S in range(i+1):  
        print(f"{5-S}" , end="")
    print()