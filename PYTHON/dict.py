info = {
    "name" : "siddhartha",
    "marks" : 99,
    "age" : 18,
    "subjects" : ["maths","science"],
    "PI" : 3.14
}

# print(info["name"])
# print(info.keys())
# print(type(info.keys()))

# print(info.values())
# print(type(info.values()))

# print(info.items())
# print(info.get("name1"))

info.update({
    "city":"delhi"
})

print(info)