# color = input("Enter color name : ")

# if color == "red":
#     print("Stop")
# elif color == "green":
#     print("Ready")
# elif color == "yellow":
#     print("Go")
# else:
#     print("only red,green,yello color accepted")


# age = int(input("Enter you age : "))

# if age >= 18:
#     print("adult")
# else:
#     print("teen")

# username = str(input("enter you username : "))
# password = int(input("enter you password : "))

# if username=="admin" and password==123:
#     print("login successfull")
# elif username != "admin":
#     print("wrong")
# else:
#     print("login faild")

# num = int(input("enter the number : "))

# # if num % 5 == 0 : 
# #     print("yes multiple of 5")
# # else:
# #     print("not multiple of 5")

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

password = input("enter the password : ")
username = input("ente the username : ")

if username == "user" and password == "pass":
    print("success")
else:
    if password != "pass":
        print("wrong password")
    else:
        print("wront username")