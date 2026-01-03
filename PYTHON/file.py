# f = open("sample.txt","r")

# data = f.read()

# print(data)

# f = open("sample.txt","a")

# f.write("\nanothher new task of python code")


f = open("sample.txt","r+")

f.write("123")

print(f.read())